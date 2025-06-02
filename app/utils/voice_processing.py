# Functions for transcribing voice with Whisper

import whisper

model = whisper.load_model("base")
result = model.transcribe("voice_memo.m4a")
voice_command = result["text"]

if __name__ == '__main__':
    print(voice_command)
