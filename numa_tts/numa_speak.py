import torch
import json
import numpy as np
import soundfile as sf
import os
import sys

# ➕ Ajout du dossier HiFi-GAN dans le path
sys.path.append(os.path.abspath("hifigan"))

from models import Generator
from env import AttrDict

from TTS.config import load_config
from TTS.utils.audio import AudioProcessor
from TTS.tts.models.vits import Vits

# 📁 Chemins de tes modèles
TTS_MODEL_PATH = r"C:\Users\trist\Documents\S910\Numa-Project\numa_tts\TTS\runs\vits_numa_v2\vits_numa_expressive_v2-April-01-2025_04+39PM-dbf1a08a\best_model.pth"
TTS_CONFIG_PATH = r"C:\Users\trist\Documents\S910\Numa-Project\numa_tts\TTS\runs\vits_numa_v2\vits_numa_expressive_v2-April-01-2025_04+39PM-dbf1a08a\config.json"

VOCODER_PATH = r"C:\Users\trist\Documents\S910\Numa-Project\numa_tts\hifigan\UNIVERSAL_V1\g_02500000"
VOCODER_CONFIG = r"C:\Users\trist\Documents\S910\Numa-Project\numa_tts\hifigan\UNIVERSAL_V1\config.json"

TEXT = "You survived the day. Gold star."
OUTPUT_WAV = "final_output.wav"

# 🎛️ Config vocoder
with open(VOCODER_CONFIG) as f:
    vocoder_config = json.load(f)
vocoder_config = AttrDict(vocoder_config)

# 🔧 Load vocoder HiFi-GAN
generator = Generator(vocoder_config)
checkpoint = torch.load(VOCODER_PATH, map_location="cpu")
if "generator" in checkpoint:
    generator.load_state_dict(checkpoint["generator"])
else:
    generator.load_state_dict(checkpoint)
generator.eval()
generator.remove_weight_norm()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
generator.to(device)

# 🔊 Fonction de vocodage
def vocode(mel_tensor):
    with torch.no_grad():
        mel_tensor = mel_tensor.to(device)
        audio = generator(mel_tensor).squeeze().cpu().numpy()
    return audio

# 🧠 Chargement du modèle VITS
config = load_config(TTS_CONFIG_PATH)
ap = AudioProcessor.init_from_config(config)
vits = Vits.init_from_config(config)
vits.load_checkpoint(config, TTS_MODEL_PATH, eval=True)
vits.eval()
vits.to(device)

# 📝 Texte → mel spectrogramme
# 📝 Texte → mel spectrogramme
input_ids = vits.tokenizer.text_to_ids(TEXT)
input_tensor = torch.LongTensor(input_ids).unsqueeze(0).to(device)

with torch.no_grad():
    result = vits.inference(input_tensor)
    audio = result["model_outputs"].squeeze().cpu().numpy()



sf.write(OUTPUT_WAV, audio, ap.sample_rate)
print(f"✅ WAV file generated at: {OUTPUT_WAV}")
