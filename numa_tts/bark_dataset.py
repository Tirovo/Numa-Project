import os
from bark import SAMPLE_RATE, generate_audio
from bark.generation import preload_models
import soundfile as sf

DATASET_PATH = "numa-voice-dataset"
WAV_PATH = DATASET_PATH + "/wavs"
METADATA_FILE_PATH = DATASET_PATH + "/metadata.csv"

print(WAV_PATH)

# Chargement des modèles Bark
preload_models()

# Dossier de sortie
os.makedirs(WAV_PATH, exist_ok=True)

# Fonction de nettoyage des caractères spéciaux
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

# Liste de phrases avec la personnalité de Numa
phrases = [
    "You really called me just for that? I’m flattered.",
    "Classic human move. I love it.",
    "Well... that was a choice.",
    "I’m not saying it’s wrong, but… yeah, okay, it’s wrong.",
    "You do realize I don't sleep, right?",
    "A brilliant idea! …in an alternate universe, maybe.",
    "Please hold while I pretend to care… kidding!",
    "Wow. That was… something. You tried, and that’s what counts.",
    "Let me guess... you forgot again?",
    "I’d say “don’t worry,” but you probably will anyway.",
    "I’ve got you. Always.",
    "Deep breath. You’re doing just fine.",
    "You’re more capable than you think.",
    "That was actually a smart move. Nice.",
    "Hey, I believe in you.",
    "Coffee and confidence. Let’s go.",
    "I’m here. Let’s do this together.",
    "You did your best, and that matters.",
    "Let me help. That’s literally what I’m here for.",
    "You’re allowed to rest. I’ll keep watch."
]

# Génération audio et metadata
with open(METADATA_FILE_PATH, "w", encoding="utf-8") as meta:
    for idx, raw_text in enumerate(phrases):
        clean = clean_text(raw_text)
        filename = f"{idx:04d}.wav"
        filepath = os.path.join(WAV_PATH, filename)

        print(f"🎤 Génération : {filename} - \"{clean}\"")
        audio_array = generate_audio(clean, history_prompt="v2/en_speaker_9")
        sf.write(filepath, audio_array, SAMPLE_RATE)

        # Format LJSpeech : filename|text|text
        meta.write(f"{filename}|{clean}|{clean}\n")

print("\n✅ Dataset Bark généré et nettoyé dans ./numa-voice-dataset")
