from app.ai.speech_to_text.transcriber_factory import TranscriberFactory
from app.ai.text_to_speech.speaker_factory import SpeakerFactory


def main():
    transcriber = TranscriberFactory.create()
    speaker = SpeakerFactory.create()

    text = transcriber.transcribe("sample.wav")

    print(text)

    speaker.speak(text)


if __name__ == "__main__":
    main()