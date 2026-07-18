from app.ai.speech_to_text.whisper_transcriber import WhisperTranscriber


class TranscriberFactory:

    @staticmethod
    def create(engine: str = "whisper"):
        if engine == "whisper":
            return WhisperTranscriber()

        raise ValueError(f"Unsupported transcriber: {engine}")