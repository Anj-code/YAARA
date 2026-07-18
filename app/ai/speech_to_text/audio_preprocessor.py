class AudioPreprocessor:
    """
    Handles preprocessing of audio before transcription.
    """

    def preprocess(self, audio_path: str) -> str:
        """
        Preprocess the audio file.

        Returns:
            Path of processed audio.
        """
        return audio_path