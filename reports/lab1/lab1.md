# Lab 1: Unix Introduction

## Tasks
1. Create a directory structure for this lab in your home directory using mkdir and cd. There should be a directory for the course, and within it a directory for each lab. 

    We'll start with making the course folder, with a reports directory holding directories for each lab. We'll write the reports using markdown.
    ```shell
    mkdir appbio && cd appbio
    mkdir reports && cd reports
    mkdir lab1 && cd lab1
    touch lab1.md
    ```

    Next we'll have a src folder for the code and a data folder for data.
    ```shell
    cd ~/appbio/
    mkdir src
    mkdir data
    ```

2. Use the man command to figure out...
  
  * ... what the command "ls -l" does.
    
    The `ls` command lists the contents of a directory. For example `ls ~/appbio/` will list the course directory contents. Using the `-l` argument uses the 'long listing' format. This shows the contents of the directory as well as permissions, file size, owner, group owner, and modification date. 

  
  * ... how you delete a directory and its contents with rm.
    
    The `rm` command removes files or directories. To remove a file, just use `rm filename.file`. You can use wildcards to remove multiple files: 
    ```bash
    touch {a..z}.test
    rm *.test
    ```

    To delete a directory we have to use the `-r` argument, which stands for recursive. This is necessary to delete even empty directories.

    ```bash
    mkdir testdir && cd testdir
    touch {a..z}.test
    cd ..
    rm -r testdir
    ```


3. Find out, perhaps using man, what the following commands are for.

    * cat

    concantenates files and sends them to stdout

    * more or less

    more is for reading through text one screenful at a time. less is an extended version of more (which is confusing, but i guess you could say less is more)

    * head

    Shows the first 10 lines of a file. You can use the `-n` argument to specify the number of lines, e.g. `head -n 20 somefile.txt`

    * tail

    Shows the last 10 lines of a file. You specify the number of lines with `-n` otherwise.

    * wc

    Outputs number of newlines, words, and byte counts for a given file

    * grep

    Search a file using regular expression patterns. Any lines which match the pattern will be output.

    * sort

    Given a text file, `sort` will sort the lines of the file.

    * uniq

    Given a file, it will report/omit the lines which are repeating that are _adjacent_. We can use `sort` to make non-adjacent lines, adjacent.

    * cut

    Remove sections from each line of files and print them to standard output. This could be considered a shortcut for what would be some regular expression patterns when using `grep`. Example usages of `cut` are for removing the first column of a file, `cut -c1 somefile.test`. You can extract specific fields from a file if fields are delimited by ':' `cut -d':' -f1 somefile.test`. The `-d` argument specifies the delimiter and the `-f` argument specifies the field number.

# Working in Unix

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