import os
import sys
from utils import check_file_exists
from moviepy.editor import VideoFileClip

# Supported video extensions
VIDEO_EXTENSIONS = (".mp4", ".avi", ".mkv", ".mov",
                    ".wmv", ".qt", ".mp4", ".mpeg")


def convert_video_to_audio_moviepy(video_file, output_ext="mp3"):
    """Converts video to audio using MoviePy library that uses `ffmpeg` under the hood"""
    filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)
    # TODO: Manage the output file name
    file_name = filename + "." + output_ext
    clip.audio.write_audiofile(file_name, verbose=False, logger=None)
    return file_name


def check_video(file):
    """Checks if the file is a video with a supported extension"""
    # ?If the file is already an audio file, then we don't need to convert it
    if not file.endswith(VIDEO_EXTENSIONS):
        print(f"File {file} is not a video")
        sys.exit(1)


# --------------------- Main function ---------------------
def audio_conversion(video):
    """Converts video to audio"""
    print("Converting video to audio...")
    check_file_exists(video)
    check_video(video)
    file_name = convert_video_to_audio_moviepy(video)
    # TODO: Once the conversion is done, delete the video file
    print("Conversion complete")
    return file_name
