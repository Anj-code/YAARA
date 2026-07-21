from app.ai.speech_to_text.whisper_transcriber import WhisperTranscriber


class TranscriberFactory:

    @staticmethod
    def create():
        return WhisperTranscriber()