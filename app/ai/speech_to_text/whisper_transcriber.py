from app.ai.speech_to_text.base_transcriber import BaseTranscriber


class WhisperTranscriber(BaseTranscriber):

    def __init__(self):
        self.model = None

    def load_model(self):
        print("Loading Whisper model...")

    def transcribe(self, audio_path: str) -> str:
        print(f"Transcribing {audio_path}")

        # Whisper code will go here later

        return "Dummy transcription"