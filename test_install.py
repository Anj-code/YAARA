import whisper
import edge_tts
import torch
import sounddevice

print("Whisper:", whisper.__version__ if hasattr(whisper, "__version__") else "OK")
print("Torch:", torch.__version__)
print("Edge TTS: OK")
print("SoundDevice: OK")

print("\nYAARA Environment Ready 🚀")