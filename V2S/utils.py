import sys
import os


def check_file_exists(file):
    """Checks if file exists"""
    if not os.path.exists(file):
        print(f"File {file} does not exist")
        sys.exit(1)
    else:
        print(f"File {file} exists")


def set_tensorflow_log_level(level):
    """Sets the log level for Tensorflow"""
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = level
