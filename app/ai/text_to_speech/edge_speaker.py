import os
import edge_tts

from app.ai.text_to_speech.base_speaker import BaseSpeaker


class EdgeSpeaker(BaseSpeaker):

    async def speak(self, text: str):

        communicate = edge_tts.Communicate(
            text=text,
            voice="en-IN-PrabhatNeural"
        )

        await communicate.save("response.mp3")

        os.startfile("response.mp3")