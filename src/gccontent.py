# TODO: Print GC output from a sequence, formatted with ~4 decimal places
import os

def get_data(filename):
    """Returns a filehandler from ../data/filename if it exists"""
    pass

def is_valid_file(file, parser):
    if not os.path.exists(file):
        parser.error(f"Could not find the file: {file}")    
    return file

if __name__ == '__main__':
    import argparse
    import fasta_reader

    parser = argparse.ArgumentParser(description='Compute GC content of a DNA sequence')
    parser.add_argument('files', nargs='+', help='File or list of files to be processed', type=lambda f: is_valid_file(f, parser))
    args = parser.parse_args()

    readers = []
    for file in args.files:
        reader = fasta_reader.FastaReader()
        reader.read_file(file)
        readers.append(reader)
    for reader in readers:
        for name, sequence in reader.sequences.items():
            print(sequence.gc_content)