# Description: Converts video to audio using MoviePy library

import os
import sys
from moviepy.editor import VideoFileClip

# Supported video extensions
VIDEO_EXTENSIONS = (".mp4", ".avi", ".mkv", ".mov", ".wmv", ".qt", ".mp4", ".mpeg")

def convert_video_to_audio_moviepy(video_file, output_ext="mp3"):
    """Converts video to audio using MoviePy library that uses `ffmpeg` under the hood"""
    filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(f"{filename}.{output_ext}")


if __name__ == "__main__":
    file = sys.argv[1]
    
    # Check if file exists
    if not os.path.exists(file):
        print(f"File {file} does not exist")
        sys.exit(1)
        
    # Check if file is a video
    # ?If the file is already an audio file, then we don't need to convert it
    if not file.endswith(VIDEO_EXTENSIONS):
        print(f"File {file} is not a video")
        sys.exit(1)        
        
    # Convert video to audio
    convert_video_to_audio_moviepy(file)
    
    #TODO: Once the conversion is done, delete the video file