from app.ai.speech_to_text.audio_recorder import AudioRecorder
from app.ai.speech_to_text.transcriber_factory import TranscriberFactory


def main():
    recorder = AudioRecorder()

    audio_path = "sample.mpeg"

    transcriber = TranscriberFactory.create()

    text = transcriber.transcribe(audio_path)

    if not text.strip():
        print("⚠️ No speech detected.")
    else:
        print(f"You said: {text}")


if __name__ == "__main__":
    main()