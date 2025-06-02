# Functions for transcribing voice with Whisper

import whisper
import certifi

model = whisper.load_model("base")
result = model.transcribe("VoiceMemoFile.m4a")
voice_command = result["text"]

if __name__ == '__main__':
    print(voice_command)
