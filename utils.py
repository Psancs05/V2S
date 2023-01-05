import sys
import os

def check_file_exists(file):
    """Checks if file exists"""
    if not os.path.exists(file):
        print(f"File {file} does not exist")
        sys.exit(1)