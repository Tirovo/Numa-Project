import sounddevice as sd
import numpy as np
import queue
import threading
import time
import sys

import torch
from faster_whisper import WhisperModel

sys.stdout.reconfigure(encoding='utf-8')

model, utils = torch.hub.load(
    repo_or_dir='snakers4/silero-vad',
    model='silero_vad',
    force_reload=False
)
(get_speech_timestamps, _, _, _, _) = utils

SAMPLE_RATE = 16000
BLOCK_DURATION = 0.5
BLOCK_SIZE = int(SAMPLE_RATE * BLOCK_DURATION)

audio_queue = queue.Queue()
vad_buffer = []

whisper_model = WhisperModel("large", device="cuda", compute_type="float16")

def audio_callback(indata, frames, time_info, status):
    if status:
        print(f"Audio status: {status}")
    audio_queue.put(indata[:, 0].copy())

def transcription_loop():
    speaking = False
    buffer = []
    silence_duration = 0.0
    max_silence = 1.0

    while True:
        data = audio_queue.get()

        try:
            vad_buffer.append(torch.from_numpy(data).float())

            if len(vad_buffer) == 0:
                continue

            audio_tensor = torch.cat(vad_buffer)[-SAMPLE_RATE * 3:]
            speech_timestamps = get_speech_timestamps(audio_tensor, model, sampling_rate=SAMPLE_RATE)

            if speech_timestamps:
                speaking = True
                buffer.append(data)
                silence_duration = 0.0
            elif speaking:
                silence_duration += BLOCK_DURATION
                if silence_duration > max_silence:
                    print("Transcription...")
                    full_audio = np.concatenate(buffer, axis=0)
                    segments, _ = whisper_model.transcribe(full_audio, language="en")

                    for seg in segments:
                        print(seg.text)

                    buffer.clear()
                    vad_buffer.clear()
                    speaking = False
        except Exception as e:
            print(f"Transcription mistake: {e}")

if __name__ == "__main__":
    print("Numa is listening... Talk to her.")

    threading.Thread(target=transcription_loop, daemon=True).start()

    try:
        with sd.InputStream(
            callback=audio_callback,
            channels=1,
            samplerate=SAMPLE_RATE,
            blocksize=BLOCK_SIZE
        ):
            while True:
                time.sleep(0.1)
    except KeyboardInterrupt:
        print("Manual stop.")
    except Exception as e:
        print(f"Micro mistake : {e}")
