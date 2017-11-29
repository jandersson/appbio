from fasta_reader import FastaReader
from dnasequence import to_fasta

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
    'UAA': '', 'UAG': '', 'UGA': '',
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
    best_length = 0
    best_start = 0
    best_stop = ""
    for start_index in start_indices:
        for stop_codon in stop_codons:
            length = orf_length(sequence[start_index:], stop_codon)
            if length > best_length:
                best_length = length
                best_start = start_index
                best_stop = stop_codon
    return sequence[best_start:best_start+best_length-1]

def translate_to_aa(sequence):
    acid_list = []
    for offset in range(3):
        codons = [sequence[i:i+3] for i in range(offset, len(sequence), 3)]
        acids = ''.join([codon_to_aa(codon) for codon in codons])
        acid_list.append(acids)
    return max(acid_list, key=len)

if __name__ == '__main__':
    import os
    data_path = os.path.join(os.path.dirname(__file__), os.pardir, 'data')
    test_files = ['translationtest.dna']
    for data_file in test_files:
        reader = FastaReader()
        data = os.path.join(data_path, data_file)
        reader.read_file(data)
        for name, sequence in reader.sequences.items():
            acids = translate_to_aa(sequence)
            print(to_fasta(name, acids))
    