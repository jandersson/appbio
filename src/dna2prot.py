
if __name__ == '__main__':
    from Bio import SeqIO
    import warnings
    warnings.filterwarnings("ignore")
    from common import is_valid_file
    import argparse

    parser = argparse.ArgumentParser(description='Open and print a FASTA file')
    parser.add_argument('file', type=lambda f: is_valid_file(f, parser),
                        help='File in FASTA format')
    args = parser.parse_args()

    with open(args.file, "rU") as handle:
        for record in SeqIO.parse(handle, 'fasta'):
            record.seq = record.seq.translate()
            print(record.format('fasta'))

