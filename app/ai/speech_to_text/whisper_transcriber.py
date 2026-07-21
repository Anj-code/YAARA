import whisper

from app.ai.speech_to_text.base_transcriber import BaseTranscriber


class WhisperTranscriber(BaseTranscriber):

    def __init__(self, model_name="base"):
        print(f"Loading Whisper model ({model_name})...")
        self.model = whisper.load_model(model_name)
        print("Whisper model loaded.\n")

    def transcribe(self, audio_path):
        print(f"Transcribing: {audio_path}")

        result = self.model.transcribe(
            audio_path,
            fp16=False,
            language="en"
        )

        return result["text"].strip()