import os
import subprocess
import soundfile as sf
import numpy as np
from bark import SAMPLE_RATE, generate_audio
from bark.generation import preload_models

# Dossiers
DATASET_DIR = "numa-voice-dataset-test"
RAW_WAV_DIR = os.path.join(DATASET_DIR, "wavs")
PITCHED_DIR = "numa-voice-dataset-highpitch-sox-test/wavs"
METADATA_PATH = os.path.join("numa-voice-dataset-highpitch-sox-test", "metadata.csv")
SENTENCES_PATH = "bark_sentences.txt"

os.makedirs(RAW_WAV_DIR, exist_ok=True)
os.makedirs(PITCHED_DIR, exist_ok=True)

# Chargement des modèles Bark
preload_models()

# Pitch en cents (100 cents = 1 demi-ton) et peak cible pour normalisation
PITCH_CENTS = 300
TARGET_PEAK = 0.90

# Nettoyage texte
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

# Lecture des phrases depuis un fichier texte
def read_phrases(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

# Fonction de normalisation
def normalize_wav(filepath):
    data, sr = sf.read(filepath)
    peak = np.max(np.abs(data))
    if peak > TARGET_PEAK:
        factor = TARGET_PEAK / peak
        data = data * factor
        sf.write(filepath, data, sr)
        print(f"✅ Normalisé : {os.path.basename(filepath)} (ancien peak: {peak:.3f})")
    else:
        print(f"✔️ OK : {os.path.basename(filepath)} (peak: {peak:.3f})")

# Lecture des phrases
to_speak = read_phrases(SENTENCES_PATH)

# Boucle principale de traitement
with open(METADATA_PATH, "w", encoding="utf-8") as meta:
    for idx, raw_text in enumerate(to_speak):
        clean = clean_text(raw_text)
        base_filename = f"{idx:04d}"
        full_filename = base_filename + ".wav"

        raw_path = os.path.join(RAW_WAV_DIR, full_filename)
        pitched_path = os.path.join(PITCHED_DIR, full_filename)

        print(f"\n🎤 Génération : {full_filename} - \"{clean}\"")
        audio = generate_audio(clean, history_prompt="v2/en_speaker_9")
        sf.write(raw_path, audio, SAMPLE_RATE)

        # Commande SoX : pitch + resample en 22050 Hz
        command = ["sox", raw_path, "-r", "22050", pitched_path, "pitch", str(PITCH_CENTS)]
        try:
            subprocess.run(command, check=True)
            print(f"✅ Pitché & resamplé : {base_filename}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur sur {base_filename} : {e}")
            continue

        # Normalisation du fichier pitché
        normalize_wav(pitched_path)

        # Metadata LJSpeech
        meta.write(f"{base_filename}|{clean}|{clean}\n")

print("\n✅ Tous les fichiers sont pitchés, resamplés, normalisés et stockés dans :", PITCHED_DIR)
print("📝 Metadata créé dans :", METADATA_PATH)
