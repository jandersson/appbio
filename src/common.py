import os
import argparse

def is_valid_file(file, parser):
    if not os.path.exists(file):
        parser.error(f"Could not find the file: {file}")    
    return os.path.abspath(file)

def file_parser(prog_desc=None, file_desc=None):
    parser = argparse.ArgumentParser(description=prog_desc)
    parser.add_argument('file', type=lambda f: is_valid_file(f, parser),
                        help=file_desc)
    return parser