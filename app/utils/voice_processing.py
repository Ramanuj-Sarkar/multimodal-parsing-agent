# Functions for transcribing voice with Whisper

import whisper


def process_file(filename):
    model = whisper.load_model("base")
    result = model.transcribe(filename, fp16=False)
    return result["text"]


if __name__ == '__main__':
    print(process_file("voice_memo.m4a"))
