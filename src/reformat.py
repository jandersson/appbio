import os
from stockholm_reader import StockholmReader

def is_valid_file(filename, parser):
    if not os.path.exists(filename):
        parser.error("Could not find that file")    
    else:
        reader = StockholmReader()
        reader.read_file(filename)
        return reader

if __name__ == '__main__':
    import argparse
    from fasta_writer import to_fasta

    parser = argparse.ArgumentParser(description='Read a Stockholm formatted file and output as FASTA')
    parser.add_argument('-f', help="The name of the Stockholm file", required=True, 
                        type=lambda f: is_valid_file(f, parser), dest="reader")
    args = parser.parse_args()
    for name, sequence in args.reader.sequences.items():
        print(to_fasta(name, sequence))

