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
