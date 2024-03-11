import os
import wave
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()


class Config:
    channels = 2
    sample_width = 2
    sample_rate = 44100

def save_wav_file(file_path, wav_bytes):
    with wave.open(file_path, 'wb') as wav_file:
        wav_file.setnchannels(Config.channels)
        wav_file.setsampwidth(Config.sample_width)
        wav_file.setframerate(Config.sample_rate)
        wav_file.writeframes(wav_bytes)

def transcribe(file_path):
    harvard = sr.AudioFile(file_path)
    with harvard as source:
        audio = r.record(source)
        text = r.recognize_google(audio)
        print(text)
        return text
