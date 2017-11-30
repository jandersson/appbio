import os

def is_valid_file(file, parser):
    if not os.path.exists(file):
        parser.error(f"Could not find the file: {file}")    
    return file