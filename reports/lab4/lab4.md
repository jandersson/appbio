# Python with Modules

## Translate with Biopython

Run the program

```
python src/dna2prot.py data/translationtest.dna
python src/dna2prot.py data/empty.fa
```

## A motif filter

Run the program 

```
python src/kleek_finder.py data/prots.fa
python src/kleek_finder.py data/empty.fa
python src/kleek_finder.py data/kleek.fa
```

There are 23 hits in prots.fa

## KLEEK Aligned?

1. Explain the purpose of multialignments

    They are useful for finding common ancestry via an alignment in genetic sequence. Using MSA one can assess the sequences shared evolutionary origins.

2. Does the KLEEK motif line up in your multialignment?

    Run the program to see

```
python src/kleek_align.py data/prots.fa
```

## Remote Blast

1. Figure out what Blast does and how it works.

    Sequence analysis tool. Finds similarities between sequences. Allows exploring evolutionary relationships.

    Blast does "local" alignments. This is faster than performing a global alignment (across entire sequence strings).

2. What is an e-value

It is the number of hits one can 'expect' when searching the database. An e-value of 1 means that in the given database one would expect 1 match with a similar score. When the e-value is closer to zero, the match is more significant. The length of the sequence is taken into account, so short sequences have high E values because they have a higher probability of occuring randomly. 

3. Find the highest scoring alignment

Its homo-sapiens. Looking at the alignment, one can see that only two of the proteins dont line up (theyre shown as empty spaces in the center sequence).

3. Demonstrate program

Run the program

```
python src/blast_query.py data/cst3.fa
```

## Blast Parsing

## Data Visualization Using MatPlotLib

1. Explain how the histogram is built

The program reads in the scores using BioPython. The scores are added to a list which is sent to matplotlibs histogram function. The histogram is added to a figure which is saved to pdf file. 

2. Show how you can use the results from the assignment "Remote Blast" as input to your program.

Run the program

```
python src/blast_hist.py data/blast/cst3.xml hist
evince hist.pdf
```