from app.ai.llm.llm_factory import LLMFactory
from app.ai.speech_to_text.transcriber_factory import TranscriberFactory
from app.ai.text_to_speech.speaker_factory import SpeakerFactory
import asyncio


def main():

    # Speech to Text
    transcriber = TranscriberFactory.create()
    text = transcriber.transcribe("record.mpeg")

    print(f"\nYou said: {text}")

    # LLM
    llm = LLMFactory.create()

    print("\nThinking...\n")

    reply = llm.generate_response(text)

    print("YAARA:")
    print(reply)

    # Text to Speech
    speaker = SpeakerFactory.create()
    asyncio.run(speaker.speak(reply))


if __name__ == "__main__":
    main()