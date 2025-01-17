import sounddevice as sd
import numpy as np
import wave
import os

class AudioRecorder:
    def __init__(self, filename="output.wav", duration=5, fs=44100):
        self.filename = filename
        self.duration = duration
        self.fs = fs
        self.recording = None

    def record_audio(self):
        print("Recording started...")
        self.recording = sd.rec(int(self.duration * self.fs), samplerate=self.fs, channels=2, dtype='int16')
        sd.wait()  # Wait until recording is finished
        print("Recording stopped.")

    def save_audio(self):
        if self.recording is None:
            print("No audio recorded to save.")
            return

        with wave.open(self.filename, 'wb') as wf:
            wf.setnchannels(2)
            wf.setsampwidth(2)  # 16-bit
            wf.setframerate(self.fs)
            wf.writeframes(self.recording.tobytes())
        print(f"Audio saved as {self.filename}")

    def play_audio(self):
        if self.recording is None:
            print("No audio recorded to play.")
            return

        print("Playing audio...")
        sd.play(self.recording, self.fs)
        sd.wait()
        print("Playback finished.")

    def delete_audio(self):
        if self.recording is None:
            print("No audio recorded to delete.")
            return

        self.recording = None
        print("Audio deleted.")

if __name__ == "__main__":
    recorder = AudioRecorder()
    recorder.record_audio()
    recorder.play_audio()
    recorder.save_audio()
    recorder.delete_audio()