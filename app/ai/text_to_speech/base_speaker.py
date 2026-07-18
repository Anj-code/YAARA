from abc import ABC, abstractmethod


class BaseSpeaker(ABC):
    """
    Abstract base class for all Text-to-Speech engines.
    """

    @abstractmethod
    def speak(self, text: str) -> None:
        """
        Convert text into speech.

        Parameters:
            text (str): Text to speak.
        """
        pass