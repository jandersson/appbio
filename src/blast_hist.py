if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import argparse
    from Bio.Blast import NCBIXML
    from common import is_valid_file

    parser = argparse.ArgumentParser(description='Plot a histogram of a BLAST query')
    parser.add_argument('infile', type=lambda f: is_valid_file(f, parser), help='XML file containing BLAST query results')
    parser.add_argument('outfile', help='Filename for output histogram (dont incude extension)')
    args = parser.parse_args()

    fd = open(args.infile, 'rU')
    record = list(NCBIXML.parse(fd))[0]

    # num_bins = 20
    fig, ax = plt.subplots()
    scores = []
    
    for alignment in record.alignments:
        for hsp in alignment.hsps:
            # if score isn't the needed attribute then its probably expect or bits
            scores.append(hsp.score)

    n, bins, patches = ax.hist(scores)
    ax.set_xlabel('Scores')
    ax.set_ylabel('Count')
    ax.set_title('Histogram of BLAST Scores')
    fig.tight_layout()
    plt.savefig(f"{args.outfile}.pdf")








