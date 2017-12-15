# Basic Python

# Random DNA Sequence

## Task

Write a python script that will generate a random DNA sequence and output it in FASTA format. The user should specify the length, and a name should be suggested.

edit: Ive allowed the user to specify a name. If none is given we'll generate one using a timestamp.

## Code

Since the code is relatively concise, I'll include it in this report.

```python
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

# Reading Stockholm files

## Task
Write a script that reads a Stockholm-formatted file and writes the number of sequences in it, followed by the accessions of the sequences. 

## Questions
1. What is an accession?
    An accession is a unique identifier for a polymer sequence (here it is DNA). It is like a primary key in a database.
2. Structure of a Stockholm file:
    The file consists of a header, a multiple sequence alignment, metadata (features), and footer.
    
    See more here: http://scikit-bio.org/docs/0.5.0/generated/skbio.io.format.stockholm.html

# Re-formatting sequences

## Tasks
1. Show how your program works on the four testcases.
    ```
    python src/reformat.py -f data/longseqs.sthlm
    python src/reformat.py -f data/shortseqs.sthlm
    python src/reformat.py -f data/cornercase.sthlm
    python src/reformat.py -f data/pf00041.sthlm
    ```

## Questions
1. What is pfam?

    From the homepage:

    >The Pfam database is a large collection of protein families, each represented by multiple sequence alignments and hidden Markov models (HMMs). Less...
    >
    >Proteins are generally composed of one or more functional regions, commonly termed domains. Different combinations of domains give rise to the diverse range of proteins found in nature. The identification of domains that occur within proteins can therefore provide insights into their function.
    >
    >Pfam also generates higher-level groupings of related entries, known as clans. A clan is a collection of Pfam entries which are related by similarity of sequence, structure or profile-HMM.
    >
    >The data presented for each entry is based on the UniProt Reference Proteomes but information on individual UniProtKB sequences can still be found by entering the protein accession. Pfam full alignments are available from searching a variety of databases, either to provide different accessions (e.g. all UniProt and NCBI GI) or different levels of redundancy.

# Translate DNA

## Questions
1. What are the "stop codons" in the standard code?
    
    Codons are three nucleotides, or a nucleotide triplet. A stop codon is a signal to terminate the translation into proteins. In DNA there are three stop codons: TAG, TAA, and TGA. A stop codon is sufficient to stop translation.

    https://en.wikipedia.org/wiki/Stop_codon

2. Why are we talking about a standard code?
    
    The standard code refers to the encoding scheme used by the vast majority of genes. This code maps genetic information to the genetic codes A,T,G,C. A coding sequence (CDS) is the region of DNA that is used by the ribosomal machinery to produce proteins.

3. Looking for the longest ORF is a primitive way to find genes in prokaryotic genomes. Why does it not work for eukaryotes?

    In eukaryotic genes with multiple exons, open reading frames span intro/exon regions. This means that the eukaryotic open reading frames are not continuous and interrupted by introns. This means that the search for the open reading frame needs to splice together the exon regions.
    
    https://www.biostars.org/p/47022/
    
4. Why should a real ORF finder also look at the so-called Watson-Crick complement? 

    The ORF describes all the potential amino acids that might be produced during transcription. By identifying all the possible coding sequences (CDS) we can find all the potential amino acids produced. Reading the sequence in the forward direction we can find 3 frames, and reading in the reverse (complement) direction we find the other 3.

    http://vlab.amrita.edu/?sub=3&brch=273&sim=1432&cnt=1

## Demonstration

```
(appbio) jonas@Calculon:~/appbio$ python src/dna2aa.py data/translationtest.dna
>single_stop_codon

>stopcodons
NSDNSDNSDNSDNSDNSDNSDNSDNS
>ambiguities
XXXXXXXXXXXXXXXXXX
>proteinalphabet
ARNDCQEGHILKIFPSTWYV
>proteinalphabet2
ARNDCQEGHILKIFPSTWYV
>proteinalphabet3
ARNDCQEGHILKIFPSTWYV
>tooshort

>short
NS
```

```
(appbio) jonas@Calculon:~/appbio$ python src/dna2aa.py data/an_exon.fa 
>where_is_the_exon
INSIPKLFLTVLLSCLPLGWSGRIVETEEIAEGTGGVGTRCWLCCILKATSASLGVACGG
QATQLDVASSVLRIEQRQVRSFLWLLQQNQPITRGFGCHCPPSSQK

```

