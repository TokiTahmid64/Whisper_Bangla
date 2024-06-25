from src.transcribe.diarize import diarize_audio
from src.transcribe.transcribe import transcribe_audiofiles
import sys
import shutil

if __name__ == "__main__":
    audio_path, model_path = sys.argv[1], sys.argv[2]

    diarized_files = diarize_audio(audio_path)
    conversation = transcribe_audiofiles(diarized_files, model_path)
    conv_str = "\n".join([f"{name}: {text}" for name, text in conversation])
    # print the conversation to a file. Rename the file with the same name as the audio file
    with open(f"{audio_path}.txt", "w") as f:
        f.write(conv_str)

