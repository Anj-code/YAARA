from app.ai.text_to_speech.edge_speaker import EdgeSpeaker


class SpeakerFactory:

    @staticmethod
    def create(engine: str = "edge"):
        if engine == "edge":
            return EdgeSpeaker()

        raise ValueError(f"Unsupported speaker: {engine}")