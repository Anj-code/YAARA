from app.ai.llm.llm_factory import LLMFactory
from app.ai.speech_to_text.transcriber_factory import TranscriberFactory


def main():

    transcriber = TranscriberFactory.create()

    text = transcriber.transcribe("sample.mpeg")

    print(f"\nYou said: {text}")

    llm = LLMFactory.create()

    print("\nThinking...\n")

    reply = llm.generate_response(text)

    print("YAARA:")
    print(reply)


if __name__ == "__main__":
    main()