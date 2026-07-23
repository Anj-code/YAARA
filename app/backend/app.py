from app.ai.llm.llm_factory import LLMFactory
from app.memory.conversation_memory import ConversationMemory
from app.ai.speech_to_text.transcriber_factory import TranscriberFactory
from app.ai.text_to_speech.speaker_factory import SpeakerFactory

import asyncio


def main():

    print("=" * 50)
    print("🌸 YAARA 🌸")
    print("A friend you didn't know you needed.")
    print("Type 'bye' anytime to leave.")
    print("=" * 50)

    transcriber = TranscriberFactory.create()
    llm = LLMFactory.create()
    speaker = SpeakerFactory.create()
    memory = ConversationMemory()

    while True:

        # text = input("\nYou: ")
        text = transcriber.transcribe("sample.mpeg")

        if not text.strip():
            continue

        if text.lower() in ["bye", "exit", "quit", "good night"]:

            farewell = (
                "Take care of yourself, okay? "
                "I'll be here whenever you want to talk. Bye!"
            )

            print("\nYAARA:")
            print(farewell)

            asyncio.run(speaker.speak(farewell))
            break

        print("\n🌸 YAARA is thinking...\n")

        reply = llm.generate_response(
            text,
            memory_context=memory.get_context()
        )

        memory.add_user_message(text)
        memory.add_yaara_message(reply)

        print("YAARA:")
        print(reply)

        asyncio.run(speaker.speak(reply))


if __name__ == "__main__":
    main()