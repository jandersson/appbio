# More Python

## Compatability

### Questions

1. What does the program neighbor do? You only need to explain what it tries to compute, not how it does it.

    Neighbor computes a phylogenetic or evolutionary tree. 

    https://en.wikipedia.org/wiki/Phylogenetic_tree

2. What can you say about the output.

    The output is a tree.

### Demonstration

Show the distance matrix

```
(appbio) jonas@Calculon:~/appbio$ python src/basedist.py data/fly.fa data/human.fa data/ecoli.fa data/thermus.fa data/mouse.fa data/yeast.fa data/plasmodium.fa
   7
Fly       0.000     0.014     0.031     0.112     0.017     0.054     0.081     
Hsapiens  0.014     0.000     0.042     0.126     0.009     0.041     0.073     
Ecoli     0.031     0.042     0.000     0.088     0.039     0.083     0.111     
Thermus_th0.112     0.126     0.088     0.000     0.126     0.166     0.182     
Mus_muscul0.017     0.009     0.039     0.126     0.000     0.044     0.079     
Yeast     0.054     0.041     0.083     0.166     0.044     0.000     0.048     
Plasmodium0.081     0.073     0.111     0.182     0.079     0.048     0.000     
```

Write the distance matrix to a file and run the neighbor program

```
(appbio) jonas@Calculon:~/opt/phylip-3.696/exe$ python src/basedist.py data/fly.fa data/human.fa data/ecoli.fa data/thermus.fa data/mouse.fa data/yeast.fa data/plasmodium.fa >> ~/opt/phylip-3.696/exe/infile && cd ~/opt/phylip-3.696/exe/ && ./neighbor
Settings for this run:
  N       Neighbor-joining or UPGMA tree?  Neighbor-joining
  O                        Outgroup root?  No, use as outgroup species  1
  L         Lower-triangular data matrix?  No
  R         Upper-triangular data matrix?  No
  S                        Subreplicates?  No
  J     Randomize input order of species?  No. Use input order
  M           Analyze multiple data sets?  No
  0   Terminal type (IBM PC, ANSI, none)?  ANSI
  1    Print out the data at start of run  No
  2  Print indications of progress of run  Yes
  3                        Print out tree  Yes
  4       Write out trees onto tree file?  Yes


  Y to accept these or type the letter for one to change
Y

neighbor: the file "outtree" that you wanted to
     use as output tree file already exists.
     Do you want to Replace it, Append to it,
     write to a new File, or Quit?
     (please type R, A, F, or Q) 
R

Cycle   4: species 6 (   0.01020) joins species 7 (   0.03780)
Cycle   3: species 3 (   0.00288) joins species 4 (   0.08512)
Cycle   2: species 1 (   0.00183) joins node 3 (   0.02567)
Cycle   1: node 1 (   0.00912) joins species 5 (   0.00488)
last cycle:
 node 1  (   0.00188) joins species 2  (   0.00225) joins node 6  (   0.03075)

Output written on file "outfile"

Tree written on file "outtree"

Done.
```
Look at the output
```
(appbio) jonas@Calculon:~/opt/phylip-3.696/exe$ cat outfile

   7 Populations

Neighbor-Joining/UPGMA method version 3.696


 Neighbor-joining method

 Negative branch lengths allowed


    +Ecoli     
  +-2 
  ! +----Thermus_th
  ! 
  ! +Mus_muscul
  3-4 
  ! ! +Hsapiens  
  ! +-5 
  !   ! +Yeast     
  !   +-1 
  !     +-Plasmodium
  ! 
  +Fly       


remember: this is an unrooted tree!

Between        And            Length
-------        ---            ------
   3             2            0.02567
   2          Ecoli           0.00288
   2          Thermus_th      0.08512
   3             4            0.00912
   4          Mus_muscul      0.00488
   4             5            0.00188
   5          Hsapiens        0.00225
   5             1            0.03075
   1          Yeast           0.01020
   1          Plasmodium      0.03780
   3          Fly             0.00183
```

## Controlling Phylip Programs
