from abc import ABC, abstractmethod


class BaseTranscriber(ABC):
    """
    Abstract base class for all Speech-to-Text engines.
    Every transcriber must implement the transcribe() method.
    """

    @abstractmethod
    def transcribe(self, audio_path: str) -> str:
        """
        Convert an audio file into text.

        Parameters:
            audio_path (str): Path to the audio file.

        Returns:
            str: Transcribed text.
        """
        pass