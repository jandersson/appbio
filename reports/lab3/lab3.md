# Lab 3: Random DNA Sequence

## Code

Since the code is relatively concise, I'll include it in this report.

```python
import random
import argparse
import re

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

parser = argparse.ArgumentParser(description='Print a random DNA sequence in FASTA format')
parser.add_argument('--length', dest='length', default=None, type=int, help='Length of the DNA sequence')
parser.add_argument('--name', dest='name', help='Name of the sequence')
args = parser.parse_args()

if not args.length:
    length = int(input("Length: "))
else:
    length = args.length

if not args.name:
    name = input("Name: ")
else:
    name = args.name

sequence = generate_sequence(length)
fasta_string = to_fasta(name, sequence)
print(fasta_string)
```

## Output
```powershell
PS C:\Users\jaamo\appbio> & C:/Users/jaamo/AppData/Local/Programs/Python/Python36/python.exe c:/Users/jaamo/appbio/src/randomdna.py --name "Random DNA Sequence" --length 200
>Random DNA Sequence
GTCTAGCTTCGAATAAAGCCACTACATTCGTGAATGGGCCCTGTGCAGATAGGGACGCCGTGTCCGCCATTCAGGCTTTC
CTAGGCTACGACAGAACTGGGCCTTGTTCGCTTCTTGAAGTCTGTAGCGCTCGCCATGATCTGGGAGGAGTGTTCTCCAG
CACCCTTTAGGACTCTAATGATAATTCTTGGACAGACAGA
```

## Discussion
1. Which function do you find most useful for this assignment?
    The `choice` function in the `random` module worked well for doing sampling with replacement. The `re.sub` function allowed me to easily format the data to FASTA by inserting a line break every 80 characters. The `argparse` module was good for creating a command line application, allowing for a user-defined sequence length and name.

2. What distribution do you want for the nucleotides?

    According to the Wikipedia article on GC Skew: 
    >GC skew is when the nucleotides Guanine and Cytosine are over- or under-abundant in a particular region of DNA or RNA. In equilibrium conditions (without mutational or selective >pressure and with nucleotides randomly distributed within the genome) there is an equal frequency of the four DNA bases (Adenine, Guanine, Thymine, and Cytosine) on both single >strands of a DNA molecule.

    The key text is that there could be an equal frequency of the four bases. This suggests a uniform distribution, where each sample from the distribution is taken with equal probability. The `random.choice` sampling function defaults to uniform sampling.