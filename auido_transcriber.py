import sys
import os
import whisper

file = sys.argv[1]

# Check if file exists
if not os.path.exists(file):
    print(f"File {file} does not exist")
    sys.exit(1)

model = whisper.load_model("small")

# TODO: Handle audio language
# TODO: Model size

print("Transcribing audio file...")
result = model.transcribe(file)

with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])
print("Transcription complete")