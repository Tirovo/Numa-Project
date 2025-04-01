import torch
import json
import numpy as np
import soundfile as sf
import os
import sys

# ➕ Permet d'importer depuis le dossier "hifigan"
sys.path.append(os.path.abspath("hifigan"))

from models import Generator
from env import AttrDict

# 📁 Fichiers universels
config_path = "hifigan/UNIVERSAL_V1/config.json"
checkpoint_path = "hifigan/UNIVERSAL_V1/g_02500000"

# ✅ Config
with open(config_path) as f:
    h = json.load(f)
h = AttrDict(h)

# 🔧 Modèle
generator = Generator(h)
checkpoint = torch.load(checkpoint_path, map_location="cpu")
generator.load_state_dict(checkpoint['generator'])
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

# Exemple :
# audio = vocode(mel)
# sf.write("output.wav", audio, 22050)
