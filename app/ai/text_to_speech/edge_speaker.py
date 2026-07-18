from app.ai.text_to_speech.base_speaker import BaseSpeaker


class EdgeSpeaker(BaseSpeaker):

    def speak(self, text: str) -> None:
        print(f"Speaking: {text}")