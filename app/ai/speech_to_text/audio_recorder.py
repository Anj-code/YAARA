import sounddevice as sd
import soundfile as sf
import numpy as np

class AudioRecorder:
    def __init__(self):
        device = sd.query_devices(kind="input")
        self.sample_rate = int(device["default_samplerate"])

    def record(self, duration=5, output_file="recording.wav"):
        print("🎤 Listening...")
        print(f"Using sample rate: {self.sample_rate}")

        audio = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1,
            dtype="float32"
        )

        sd.wait()


        print("Max amplitude:", np.max(np.abs(audio)))

        sf.write(output_file, audio, self.sample_rate)

        print(f"Recording saved as {output_file}")

        return output_file