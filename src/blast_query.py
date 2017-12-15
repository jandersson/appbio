if __name__ == '__main__':
    from common import file_parser
    from Bio import SeqIO
    from Bio.Blast.NCBIWWW import qblast

    parser = file_parser(prog_desc='Perform a BLAST query', file_desc='A file containing a protein sequence')
    args = parser.parse_args()

    sequence = open(args.file, 'rU').read()
    result_handle = qblast('blastp', 'nr', sequence)
    print(result_handle.read())
    result_handle.close()
