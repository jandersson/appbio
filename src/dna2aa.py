from fasta_reader import FastaReader
from fasta_writer import to_fasta

rna_to_aa = {
    'UUU': 'F', 'UUC': 'F',
    'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'I',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y',
    'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop',
    'CAU': 'H', 'CAC': 'H',
    'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N',
    'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D',
    'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C',
    'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S',
    'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

def codon_to_aa(codon):
    """Translate a codon to an amino acid. Return 'X' if the codon is ambiguous"""
    if len(codon) != 3:
        return ''
    codon = codon.upper().replace('T', 'U')
    return rna_to_aa.get(codon, 'X')

def translate_to_aa(sequence):
    acid_list = []
    for offset in range(3):
        codons = [sequence[i:i+3] for i in range(offset, len(sequence), 3)]
        acids = ''
        for codon in codons:
            acid = codon_to_aa(codon)
            if acid == 'Stop':
                # break
                acid_list.append(acids)
                acids = ''
            else:
                acids += acid
        acid_list.append(acids)
    # return acid_list
    return max(acid_list, key=len)

if __name__ == '__main__':
    import os
    import argparse
    from common import is_valid_file

    parser = argparse.ArgumentParser(
        description='Find the longest open reading frame in a list of FASTA files'
        )
    parser.add_argument('files', nargs='+', help="List of FASTA files to search",
                        type=lambda f: is_valid_file(f, parser))
    args = parser.parse_args()
    for data_file in args.files:
        reader = FastaReader()
        reader.read_file(data_file)
        for name, sequence in reader.sequences.items():
            acids = translate_to_aa(sequence.sequence)
            print(to_fasta(name, acids))
            print(len(acids))
    