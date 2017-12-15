if __name__ == '__main__':
    import re
    from Bio import SeqIO
    from common import file_parser
    import os

    parser = file_parser(prog_desc='Find sequences that contain KLEEKS', file_desc='A FASTA file containing protein sequences')
    args = parser.parse_args()

    
    kleek_filter = re.compile(r'KL[EI]{2,}K')
    hits = 0
    with open(args.file, 'rU') as fd:
        for record in SeqIO.parse(fd, 'fasta'):
            if re.search(kleek_filter, str(record.seq)):
                hits += 1
                print(record.format('fasta'))
    # print(hits)

