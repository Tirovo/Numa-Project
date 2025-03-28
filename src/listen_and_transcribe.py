# Real-time vocal recognition and transcription (Numa prototype)

import sounddevice as sd
import numpy as np
import queue
import threading
import time

import torch
from faster_whisper import WhisperModel

# --- Load Silero VAD ---
model, utils = torch.hub.load(
    repo_or_dir='snakers4/silero-vad',
    model='silero_vad',
    force_reload=False
)
(get_speech_timestamps, _, _, _, _) = utils

# --- Audio config ---
SAMPLE_RATE = 16000
BLOCK_DURATION = 0.5  # seconds
BLOCK_SIZE = int(SAMPLE_RATE * BLOCK_DURATION)

audio_queue = queue.Queue()
vad_buffer = []

# --- Whisper model (GPU) ---
whisper_model = WhisperModel("medium", device="cuda", compute_type="float16")

# --- Audio callback ---
def audio_callback(indata, frames, time_info, status):
    if status:
        print(f"udio status: {status}")
    audio_queue.put(indata[:, 0].copy())  # mono

# --- Transcription logic ---
def transcription_loop():
    speaking = False
    buffer = []
    silence_duration = 0.0
    max_silence = 1.0  # seconds of silence to mark end of speech

    while True:
        data = audio_queue.get()
        vad_buffer.append(torch.from_numpy(data).float())

        audio_tensor = torch.cat(vad_buffer)[-SAMPLE_RATE*3:]  # keep last 3 seconds

        speech_timestamps = get_speech_timestamps(audio_tensor, model, sampling_rate=SAMPLE_RATE)

        if speech_timestamps:
            speaking = True
            buffer.append(data)
            silence_duration = 0.0
        elif speaking:
            silence_duration += BLOCK_DURATION
            if silence_duration > max_silence:
                print("⏳ Transcription...")
                full_audio = np.concatenate(buffer, axis=0)
                segments, _ = whisper_model.transcribe(full_audio, language="fr")

                for seg in segments:
                    print(f">>> {seg.text}")

                buffer.clear()
                vad_buffer.clear()
                speaking = False

# --- Main ---
if __name__ == "__main__":
    print("🎙️  uma écoute... Parle-lui.")

    threading.Thread(target=transcription_loop, daemon=True).start()

    with sd.InputStream(
        callback=audio_callback,
        channels=1,
        samplerate=SAMPLE_RATE,
        blocksize=BLOCK_SIZE
    ):
        while True:
            time.sleep(0.1)
