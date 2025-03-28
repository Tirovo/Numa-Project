# 🧠 Numa – Local AI Voice Companion

**Numa** is a fully local, real-time AI voice assistant. She's not just helpful — she's got wit, sarcasm, and charm. Powered by open-source AI models and designed for privacy, Numa lives on your machine, not in the cloud.

<div align="center">
  <img src="https://img.shields.io/badge/status-private%20demo-yellow" />
  <img src="https://img.shields.io/badge/powered%20by-faster--whisper-blue" />
  <img src="https://img.shields.io/badge/LLM-GPT4All%20%7C%20Mistral%20%7C%20Nous%20Hermes%202-lightgrey" />
  <img src="https://img.shields.io/badge/runs-offline-success" />
  <img src="https://img.shields.io/badge/license-CC--BY--NC%204.0-lightgrey.svg" />
</div>

---

## 🎯 What It Does

- 🎙️ Captures your voice in real time  
- 🧠 Transcribes speech with `faster-whisper` + VAD  
- 🤖 Responds using a local LLM (GPT4All, Mistral 7B, Nous Hermes...)  
- 🗣️ Speaks fluently via neural TTS (Coqui, VITS, etc.)  
- 💻 Shows everything in a beautiful local interface (Streamlit or PyQt)

---

## ✨ Numa's Personality

- 🎭 **Adaptive Personality**  
  Numa isn’t just functional — she has a tone. She adapts to you. Chill, helpful, funny, or sharp.

- 😄 **Humor Module**  
  Occasional wit, light sarcasm, and contextual jokes — without going full Neuro-sama.

- 📡 **Network Awareness**  
  Ask Numa “Who’s connected to the Wi-Fi?”, “Is Google reachable?”, “Ping my router”...

- 🎵 **Audio Reactions & Music**  
  Request "lo-fi vibes", "ambience", or "white noise", and she’ll trigger local music or sounds.

---

## 🧠 Personality & Behavior Engine

| Feature | Tool |
|--------|------|
| Conversational base | `Nous Hermes 2` (Mistral-based) |
| Personality design | Custom system prompts (ironic, warm, helpful) |
| Instruction tuning | Custom examples to refine tone |
| Optional fine-tuning | LoRA / QLoRA (lightweight & local) |
| Inference backend | `llama.cpp` / `GPT4All` with quantized GGUF models |

Example prompt:
```text
You are Numa, a sarcastic but helpful voice assistant. You're smart, witty, and enjoy making dry jokes while assisting your user. Be clever, but don't overdo it. Use irony to make things fun, not annoying.
```

---

## 🧩 Tech Stack

| Component | Tool |
|----------|------|
| **Speech-to-text** | [`faster-whisper`](https://github.com/guillaumekln/faster-whisper) + Silero VAD |
| **LLM** | [`GPT4All`](https://gpt4all.io), `llama.cpp`, `Nous Hermes 2`, `Mistral 7B` |
| **TTS** | Coqui TTS / VITS / pyttsx3 |
| **Interface** | Streamlit / PyQt |
| **System** | 100% local, offline-first – Windows (Ryzen 9, 32GB RAM) |

---

## 🤖 Inspiration

This project was inspired by watching **[Neuro-sama](https://www.twitch.tv/vedal987)** on Twitch —  
Her real-time conversational presence made me wonder:  
> *Could I build something similar, but local, private, and mine?*

Numa is the answer.

---

## ⚠️ Disclaimer – Private Showcase Project

This repository is a **personal technical showcase**.  
It is not meant for public use, deployment, or redistribution.

### Please note:
- ⚙️ It’s optimized for a local setup
- 📦 Models are not included (see `.gitignore`)
- 🔧 No full install script is provided
- 🛠️ Adaptation and configuration are required

But that’s the point — **you get to build Numa yourself.**

---

## 🔓 License

This project is licensed under the  
**Creative Commons Attribution-NonCommercial 4.0 International License**.  
📜 https://creativecommons.org/licenses/by-nc/4.0/

You’re more than welcome to:
- Explore the code and architecture
- Learn from the way components are integrated
- Build your own ideas on top of it

However, please keep in mind:
- This repository is not intended as a plug-and-play product
- Redistribution or commercial use of the code "as-is" is not allowed
- If you use part of it or get inspired by it, a simple credit is always appreciated

> I believe in open learning. If this project helps you grow or create something even better — awesome!

---

## 🧠 Why This Project Matters

**Numa** demonstrates:
- Real-time audio streaming & speech detection
- Integration of Whisper for offline STT
- Use of powerful local LLMs for contextual dialogue
- Neural voice synthesis for natural response
- A cohesive, private-by-design architecture

---

## 📬 Author

Made with ❤️ by **Tristan Londé**  
Engineer @ ENIB  
Focused on embedded AI, offline assistants, and tech with personality.


Passionate by AI and human–machine interaction.

---
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC--BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

