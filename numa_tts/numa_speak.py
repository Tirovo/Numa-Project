import torch
import tempfile
import subprocess
import os
import sounddevice as sd
import soundfile as sf
import noisereduce as nr
from TTS.api import TTS

GPU_USAGE = torch.cuda.is_available()

# Register safe classes for PyTorch deserialization
safe_classes = []

# Importing RAdam optimizer
try:
    from TTS.utils.radam import RAdam
    safe_classes.append(RAdam)
except:
    pass 

# Try importing defaultdict (used in some model configs)
try:
    from collections import defaultdict
    safe_classes.append(defaultdict)
except:
    pass  # Ignore if not available

# Always include the base dict class
safe_classes.append(dict)

# Register these classes as safe for torch.load
torch.serialization.add_safe_globals(safe_classes)

# Initializing our model (here ts_models/en/vctk/vits)
class NumaTTS:
    def __init__(self, model_name="tts_models/en/vctk/vits", highPitch_mode=True):
        self.model_name = model_name
        self.anime_mode = highPitch_mode

        '''print(f"Loading the tts model : {self.model_name}")'''
        self.tts = TTS(model_name=self.model_name, progress_bar=True, gpu=GPU_USAGE)

        if hasattr(self.tts, "speakers"):
            self.speaker = "p240"
            print("Selected voice :", self.speaker)
        else:
            self.speaker = None

    def say(self, text):
        '''print(f"Text received : {text}")'''
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as raw_file:
            raw_path = raw_file.name

        # Synthesis
        self.tts.tts_to_file(text=text, speaker=self.speaker, file_path=raw_path)

        # Voice post-processing (pitch, tempo, reverb)
        out_path = raw_path.replace(".wav", "higher_pitch.wav")
        command = (
            f"sox {raw_path} {out_path} highpass 150 pitch 350 "
            f"tempo 1 reverb 8 20 20 30 0 0 gain -2"
        )
        subprocess.call(command, shell=True)
        os.remove(raw_path)

        # Lecture + denoise léger
        if os.path.exists(out_path):
            data, sr = sf.read(out_path)
            audio = nr.reduce_noise(y=data, sr=sr, prop_decrease=0.5)
            '''print("Playing the Audio...")'''
            sd.play(audio, samplerate=sr)
            sd.wait()
            os.remove(out_path)

        torch.cuda.empty_cache()
