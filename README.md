# Cohere Voice Assistant 🎙️🧠
A lightweight, conversational AI voice assistant built with Python. It uses Local Whisper for speech-to-text, Cohere's Command-R model for intelligent responses, and Edge TTS for natural text-to-speech synthesis.

---

## Features

* **Local Speech Recognition:** Utilizes the `SpeechRecognition` library with a local Whisper model to transcribe audio accurately.
* **Intelligent Conversation:** Integrates Cohere's `command-r-08-2024` model for context-aware, highly capable AI responses.
* **Natural Voice Synthesis:** Uses `edge-tts` (Aria Neural voice) to generate high-quality, natural-sounding speech.
* **Asynchronous Audio Streaming:** Processes and plays audio efficiently in memory using `asyncio` and `pygame` without writing temporary files to the disk.
* **Voice-Activated Shutdown:** Safely terminate the assistant by saying "quit", "exit", "stop", or "goodbye".

---

## Tech Stack

| Component | Technology / Library | Description |
| :--- | :--- | :--- |
| **Speech-to-Text** | `SpeechRecognition` (Whisper) | Captures microphone input and converts it to text. |
| **LLM Engine** | Cohere API (`cohere`) | Processes the transcribed text and generates a response. |
| **Text-to-Speech** | `edge-tts` | Converts the AI's text response into natural spoken audio. |
| **Audio Playback** | `pygame`, `asyncio` | Handles asynchronous audio stream playback in-memory. |

---

## Prerequisites

Before running the project, ensure you have the following installed:
* Python 3.8+
* A working microphone
* FFmpeg (required for Whisper and some audio processing)

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yazid0al/cohere-voice-assistant.git](https://github.com/yazid0al/cohere-voice-assistant.git)
   cd cohere-voice-assistant
