def distance_matrix(sequences):
    rows = []
    for name, sequence in sequences.items():
        row = []
        row.append(name[:10])
        for other_name, other_sequence in sequences.items():
            row.append(sequence - other_sequence)
        rows.append(row)
    print(rows)

if __name__ == '__main__':
    from common import is_valid_file
    import argparse
    from fasta_reader import FastaReader

    parser = argparse.ArgumentParser(description='Compute the composition difference between genomes')
    parser.add_argument('files', nargs='+', help='List of FASTA files', type=lambda f: is_valid_file(f, parser))
    args = parser.parse_args()

    if len(args.files) == 1:
        parser.error('You must provide at least two files')

    sequences = {}
    for file in args.files:
        reader = FastaReader()
        reader.read_file(file)
        sequences.update(reader.sequences)

    distance_matrix(sequences)