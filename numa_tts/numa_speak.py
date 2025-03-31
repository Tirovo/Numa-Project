from TTS.utils.synthesizer import Synthesizer # type: ignore
import soundfile as sf # type: ignore
import torch  # type: ignore

# Config
MODEL_PATH = r"C:\Users\trist\Documents\S910\Numa-Project\numa_tts\TTS\runs\vits_numa_v2\vits_numa_expressive_v2-March-30-2025_06+27PM-dbf1a08a\best_model.pth"
CONFIG_PATH = r"C:\Users\trist\Documents\S910\Numa-Project\numa_tts\TTS\runs\vits_numa_v2\vits_numa_expressive_v2-March-30-2025_06+27PM-dbf1a08a\config.json"
OUTPUT_WAV = "test_output.wav"
TEXT = "You survived the day. Gold star." # (Example)

# Synthetizer
synthesizer = Synthesizer(
    tts_checkpoint=MODEL_PATH,
    tts_config_path=CONFIG_PATH,
    use_cuda=torch.cuda.is_available()
)

# Create wav
wav = synthesizer.tts(TEXT)
sf.write(OUTPUT_WAV, wav, synthesizer.output_sample_rate)
print(f"WAV generated : {OUTPUT_WAV}")