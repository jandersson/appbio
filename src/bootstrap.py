if __name__ == '__main__':
    import argparse
    from common import is_valid_file

    parser = argparse.ArgumentParser(description='Run Phylip bootstrap analysis on protein alignments')
    parser.add_argument('num_replicates', type=int, help='Number of bootstrap replicates to run')
    parser.add_argument('files', nargs='+', type=lambda f: is_valid_file(f, parser),
                        help='List of protein alignment files in FASTA format')
    args = parser.parse_args()