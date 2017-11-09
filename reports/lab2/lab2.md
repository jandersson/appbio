# Lab 2: Working in Unix

## Tasks
1. Take a look at the large file /info/DD2404/appbio16/data/gpcr.tab using head. This file contains data concerning G-protein coupled receptors (Länkar till en externa sida.)Länkar till en externa sida. from a number of species.head. How many columns are there (if you count by eye)? If you work on your own computer: download this fileVisa i ett nytt fönster to work on.

    ```
    jonas@Calculon:~/appbio/data$ head gpcr.tab
    Accession       Entry name      Status  Protein names   Gene names      Organism        Length
    O42385  5H1AA_TAKRU     reviewed        5-hydroxytryptamine receptor 1A-alpha (5-HT-1A-alpha) (5-HT1A-alpha) (F1A) (Serotonin receptor 1A-alpha)        htr1aa  Takifugu rubripes (Japanese pufferfish) (Fugu rubripes)        423
    O42384  5H1AB_TAKRU     reviewed        5-hydroxytryptamine receptor 1A-beta (5-HT-1A-beta) (5-HT1A-beta) (F1B) (Serotonin receptor 1A-beta)    htr1a-B Takifugu rubripes (Japanese pufferfish) (Fugu rubripes416
    Q6XXX9  5HT1A_CANFA     reviewed        5-hydroxytryptamine receptor 1A (5-HT-1A) (5-HT1A) (Serotonin receptor 1A)      HTR1A   Canis familiaris (Dog) (Canis lupus familiaris) 423
    Q9N297  5HT1A_GORGO     reviewed        5-hydroxytryptamine receptor 1A (5-HT-1A) (5-HT1A) (Serotonin receptor 1A)      HTR1A   Gorilla gorilla gorilla (Lowland gorilla)       422
    Q0EAB6  5HT1A_HORSE     reviewed        5-hydroxytryptamine receptor 1A (5-HT-1A) (5-HT1A) (Serotonin receptor 1A)      HTR1A   Equus caballus (Horse)  422
    P08908  5HT1A_HUMAN     reviewed        5-hydroxytryptamine receptor 1A (5-HT-1A) (5-HT1A) (G-21) (Serotonin receptor 1A)       HTR1A ADRB2RL1 ADRBRL1  Homo sapiens (Human)    422
    Q64264  5HT1A_MOUSE     reviewed        5-hydroxytryptamine receptor 1A (5-HT-1A) (5-HT1A) (Serotonin receptor 1A)      Htr1a Gpcr18    Mus musculus (Mouse)    421
    Q9N298  5HT1A_PANTR     reviewed        5-hydroxytryptamine receptor 1A (5-HT-1A) (5-HT1A) (Serotonin receptor 1A)      HTR1A   Pan troglodytes (Chimpanzee)    422
    Q9N296  5HT1A_PONPY     reviewed        5-hydroxytryptamine receptor 1A (5-HT-1A) (5-HT1A) (Serotonin receptor 1A)      HTR1A   Pongo pygmaeus (Bornean orangutan)      422
    ```

    There are 7 columns: Accession, Entry name, Status, Protein names, Gene names, Organism, and Length

2. How many lines is there in the file?

    ```
    jonas@Calculon:~/appbio/data$ wc gpcr.tab
    29305  402852 3541806 gpcr.tab
    ```

    The first number output by `wc` is the number of newlines. There are 29305 lines in this file.

3. Use grep and wc to find out how many human GPCRs there are listed. Do you search for "human" or "Homo sapiens"?

   ```
   jonas@Calculon:~/appbio/data$ grep "Human" gpcr.tab | wc
   2255   37924  303482
   jonas@Calculon:~/appbio/data$ grep "Homo sapiens" gpcr.tab | wc
   2244   37707  301828
   ```
   We get 11 more hits when we search for Human instead of Homo sapiens. 

   ```
   jonas@Calculon:~/appbio/data$ grep '(Human)' gpcr.tab | wc
   2244   37707  301828
   ```

   If we include the parentheses, then we get 2244 hits same as 'Homo sapiens'. 

   ```
    jonas@Calculon:~/appbio/data$ grep -P 'HUMAN' gpcr.tab | wc
   2244   37707  301828
   ```
    We can also search the 'Entry name' column as it is formatted to include the species, but this seems like it could be an unreliable way to search.

4. How long is the shortest sequence listed in the same file? Use cut and sort!

    Length is the 7th field in the data, so we can use `cut -f7` to select this field. We don't need to specify a delimiter, because TAB delimited is the default. Then we use sort with the `-n` argument to do a numeric sort on text strings. Then finally we'll use `head` to just show the first 10 lines.

    ```
    jonas@Calculon:~/appbio/data$ cut -f7 gpcr.tab | sort -h |head
    Length
    10
    12
    13
    14
    20
    23
    23
    24
    26
    ``` 

5. How many species are named in gpcr.tab?

    The plan for this will be `cut` to select the organism field, followed by `sort` to make duplicates adjacent, then `uniq` to deduplicate, finishing with `wc`. We subtract 1 to disgregard the field name.

    ```
    jonas@Calculon:~/appbio/data$ cut -f6 gpcr.tab | sort | uniq | wc
    3493   11522  104028
    ```

6. Use a for-loop to apply multi-sequence alignment program _muscle_ to the data files in /info/appbio15/data/testatin/*.fa. Figure out what muscle does and how you run it. (Sorry, no man-pages.) You have to use a for-loop in bash. Repeated manual invocation is not allowed in this course. Each run should have its own output file.

   ```bash
   for f in ~/appbio/data/yeast_genes/*.fasta; do ~/opt/muscle -in "$f" -out "$f.output"; done
   ```  