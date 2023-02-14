import argparse

from audio_converter import audio_conversion
from audio_transcriber import audio_transcription
from text_summarization import summarization

LANGUAGES = ['en', 'es', 'fr', 'de', 'it', 'pt']

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("video_path", help="Path to the video file")
    parser.add_argument(
        '--lang', help='Language of the video. Available languages: en, es, fr, de, it, pt. Default: en', default='en', choices=LANGUAGES)

    args = parser.parse_args()
    video = args.video_path
    lang = args.lang

    # Convert the video to audio
    print("--- Converting video to audio ---")
    file = audio_conversion(video)
    print("Audio file: " + file)

    # Transcribe the audio file
    print("--- Transcribing audio file ---")
    audio_transcription(file)

    # Summarize the text
    print("--- Summarizing text ---")
    summarization(file)
