class AudioRecorder:
    """
    Handles recording audio from the microphone.
    """

    def __init__(self):
        self.sample_rate = 16000

    def record(self, duration: int = 5):
        """
        Record audio for a given duration.
        """
        print(f"Recording for {duration} seconds...")

    def save(self, filename: str):
        """
        Save recorded audio.
        """
        print(f"Saving audio to {filename}")