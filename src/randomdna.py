import random
import argparse
import re
import datetime

def generate_sequence(length):
    """Generate a random DNA sequence"""
    if length < 1: return

    alphabet = ['G', 'C', 'A', 'T']
    return ''.join(random.choices(alphabet, k=length))

def to_fasta(name, sequence):
    """Format a DNA sequence string in FASTA"""
    fasta_sequence = ""
    fasta_sequence += f">{name}\n"
    fasta_sequence += re.sub("(.{80})", "\\1\n", sequence, flags=re.DOTALL)
    return fasta_sequence

def seqname_from_time():
    """Generate a name using a timestamp"""
    name = "Random_DNA_Sequence_"
    name += re.sub(r'\s', '_', str(datetime.datetime.now()).split('.')[0])
    return name

parser = argparse.ArgumentParser(description='Print a random DNA sequence in FASTA format')
parser.add_argument('--length', dest='length', type=int, help='Length of the DNA sequence')
parser.add_argument('--name', dest='name', help='Name of the sequence')
args = parser.parse_args()

length = args.length or int(input("Length: "))
name = args.name or seqname_from_time()

sequence = generate_sequence(length)
fasta_string = to_fasta(name, sequence)
print(fasta_string)