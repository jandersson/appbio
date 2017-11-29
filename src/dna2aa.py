from fasta_reader import FastaReader

start_codon = 'ATG'
stop_codons = ['TAA', 'TAG', 'TGA']
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

def to_aa(codon):
    """Translate a codon to an amino acid. Return 'X' if the codon is ambiguous"""
    codon = codon.upper().replace('T', 'U')
    return rna_to_aa.get(codon, 'X')

def find_start_codons(sequence):
    """Make a list of the indices of all start codons in a sequence"""
    if start_codon not in sequence:
        return []

    indices = []
    index = 0
    while index < len(sequence):
        index = sequence.find(start_codon, index)
        if index == -1:
            break
        else:
            indices.append(index)
        index += 1
    return indices

def orf_length(sequence, stop_codon):
    if start_codon not in sequence:
        return 0
    if stop_codon not in sequence:
        return 0

    stop_index = sequence.find(stop_codon) + 2
    return len(sequence[:stop_index])

def find_longest_orf(sequence, start_indices):
    [orf_length(sequence, stop_codon) for stop_codon in stop_codons]


def translate_to_aa(sequence):
    aa_sequence = ""
    start_locs = find_start_codons(sequence)
    find_longest_orf(sequence, start_locs)
    return aa_sequence
    #find start codon indices
    #find longest ORF using start codon indices
    #translate longest ORF
    #split sequence into 3 character strings

if __name__ == '__main__':
    import os
    data_path = os.path.join(os.path.dirname(__file__), os.pardir, 'data')
    test_files = ['translationtest.dna']
    for data_file in test_files:
        reader = FastaReader()
        data = os.path.join(data_path, data_file)
        reader.read_file(data)
        for name, sequence in reader.sequences.items():
            translate_to_aa(sequence)
    