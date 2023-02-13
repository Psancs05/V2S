import whisper
from utils import check_file_exists, set_tensorflow_log_level


def load_model(model_size="small"):
    """Loads the model into memory"""
    global model
    model = whisper.load_model("small")
    # TODO: Model size


def write_transcript(file, result):
    """Writes the transcript to a file"""
    with open(file, "w", encoding="utf-8") as f:
        f.write(result["text"])


def transcribe_audio(file):
    """Transcribes the audio file"""
    # TODO: Handle audio language
    # TODO: Handle model parameters in transcription
    result = model.transcribe(file)
    write_transcript(file, result)


# --------------------- Main function ---------------------


def audio_transcription(file):
    """Transcribes the audio file"""
    print("Transcribing audio file... (This may take a while)")
    set_tensorflow_log_level("3")
    check_file_exists(file)
    load_model()
    transcribe_audio(file)
    print("Transcription complete")
