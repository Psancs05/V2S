import sys
from audio_converter import audio_conversion
from audio_transcriber import audio_transcription
from text_summarization import summarization

if  __name__ == "__main__":
     
     # Get the video file
     video = sys.argv[1]
     
     # Convert the video to audio
     print("--- Converting video to audio ---")
     file = audio_conversion(video)
     
     # Transcribe the audio file
     print("--- Transcribing audio file ---")
     audio_transcription(file)
     
     # Summarize the text
     print("--- Summarizing text ---")
     summarization(file)
     
     