from src.transcribe.diarize import diarize_audio
from src.transcribe.transcribe import transcribe_audiofiles
import sys
import shutil
import os

if __name__ == "__main__":
    audio_path, model_path = sys.argv[1], sys.argv[2]

    diarized_files = diarize_audio(audio_path)
    conversation = transcribe_audiofiles(diarized_files, model_path)
    conv_str = "\n".join([f"{name}: {text}" for name, text in conversation])


    # save the conversation in a file. Please rename the file to the name of the audio file

    # creta a folder to store the text files
    if not os.path.exists("text_files"):
        os.makedirs("text_files")

    text_file = audio_path.split("/")[-1].split(".")[0]

    with open(f"text_files/{text_file}.txt", "w") as f:
        f.write(conv_str)
