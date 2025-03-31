import os
import subprocess
import soundfile as sf # type: ignore
import numpy as np
from bark import SAMPLE_RATE, generate_audio # type: ignore
from bark.generation import preload_models # type: ignore

DATASET_DIR = "numa-voice-dataset"
RAW_WAV_DIR = os.path.join(DATASET_DIR, "wavs")
PITCHED_DIR = "numa-voice-dataset-highpitch-sox/wavs"
METADATA_PATH = os.path.join("numa-voice-dataset-highpitch-sox-test", "metadata.csv")
SENTENCES_PATH = "bark_sentences.txt"

os.makedirs(RAW_WAV_DIR, exist_ok=True)
os.makedirs(PITCHED_DIR, exist_ok=True)

# Preloading Bark Models
preload_models()

# 300 cents = 3 semitones (1.5 steps) => voice with higher pitch and Target peak allows the reduction of saturated noises with normalization
PITCH_CENTS = 300
TARGET_PEAK = 0.90

# Clean the text in case there's unwanted characters
def clean_text(text):
    return (
        text.replace("’", "'")
            .replace("“", '"')
            .replace("”", '"')
            .replace("…", "...")
            .replace("–", "-")
            .replace("—", "-")
            .strip()
    )

# Function to read the .txt that contains the data for the bark dataset creation
def read_phrases(path_to_the_sentences):
    with open(path_to_the_sentences, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

# Normalization to reduce saturation
def normalize_wav(filepath):
    data, sr = sf.read(filepath)
    peak = np.max(np.abs(data))
    if peak > TARGET_PEAK:
        factor = TARGET_PEAK / peak
        data = data * factor
        sf.write(filepath, data, sr)
        print(f"Normalized : {os.path.basename(filepath)} (old peak: {peak:.3f})")
    else:
        print(f"Not satured : {os.path.basename(filepath)} (new peak: {peak:.3f})")

# Read the bark_sentences.txt file
to_speak = read_phrases(SENTENCES_PATH)

# Processing loop
with open(METADATA_PATH, "w", encoding="utf-8") as meta:
    for idx, raw_text in enumerate(to_speak):
        clean = clean_text(raw_text)
        base_filename = f"{idx:04d}"
        full_filename = base_filename + ".wav" # Ensures the filename has only one .wav extension, avoids issues during the training of the TTS

        raw_path = os.path.join(RAW_WAV_DIR, full_filename)
        pitched_path = os.path.join(PITCHED_DIR, full_filename)

        print(f"\nGenerating : {full_filename} - \"{clean}\"")
        audio = generate_audio(clean, history_prompt="v2/en_speaker_9") # English female speaker. You can check the list of other speakers here : https://suno-ai.notion.site/8b8e8749ed514b0cbf3f699013548683?v=bc67cff786b04b50b3ceb756fd05f68c
        sf.write(raw_path, audio, SAMPLE_RATE) # The sample rate for bark by default is 24 kHz

        # SoX : Modify voice pitch + resample to 22050 Hz to fit the common sample rate of the VITS model we're going to train
        command = ["sox", raw_path, "-r", "22050", pitched_path, "pitch", str(PITCH_CENTS)]
        try:
            subprocess.run(command, check=True)
            print(f"Pitched & resampled : {base_filename}")
        except subprocess.CalledProcessError as e:
            print(f"Error processing {base_filename} : {e}")
            continue

        # Normalization
        normalize_wav(pitched_path)

        # Metadata with LJSpeech format
        meta.write(f"{base_filename}|{clean}|{clean}\n")

print("\nTous les fichiers sont pitchés, resamplés, normalisés et stockés dans :", PITCHED_DIR)
print("\nMetadata créé dans :", METADATA_PATH)
