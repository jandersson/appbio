# Databases

## BioMart

### Preliminaries

Definitions

Gene: A sequence of DNA or RNA

Transcript: Single stranded RNA created by transcription of DNA. Yields tRNA, mRNA, rRNA.

Protein: Molecules made up of chains of amino acid residues. Performs array of functions in organisms.

Exon: Sequence of DNA used during transcription. DNA sequence which encodes a transcript.

Intron: Sequence of DNA spliced out during transcription. DNA sequence which does not encode anything.

Untranslated Regions (UTR): A region of mRNA that is not translated into protein. They do not form the protein coding region of the gene. The 3' UTR is found following the stop codon and plays a role in the translation termination.

Alternative Transcripts: Also called alternative splicing. Alternative transcripts occur when a gene codes for multiple proteins.

Homolog: The existence of a shared ancestry between genes. Inferred among proteins or DNA by sequence similarity. Multiple sequence alignment is used to discover homologous regions.

Ortholog: Genes in different species that evolved from a common ancestral gene. Identifying orthologs helps predict gene function.

Paralog: Genes related by duplication in a genome. Paralogs evolve new functions even if related to the original one.

### Trying Ensembl BioMart

1. How many unique protein-coding genes are there then? Use filters to list those genes that have the type "protein coding".
    
    22,375

    `http://www.ensembl.org/biomart/martview/7ab87768e0f0c0d880d06e06d151cb66?VIRTUALSCHEMANAME=default&ATTRIBUTES=hsapiens_gene_ensembl.default.feature_page.ensembl_gene_id|hsapiens_gene_ensembl.default.feature_page.ensembl_transcript_id&FILTERS=hsapiens_gene_ensembl.default.filters.biotype."protein_coding"&VISIBLEPANEL=filterpanel`

2. How many of the protein coding genes have been assigned an ID by the Human Gene Nomenclature Committee (HGNC)? (There should be fewer than in the previous question.)

    21,604

    `http://www.ensembl.org/biomart/martview/7ab87768e0f0c0d880d06e06d151cb66?VIRTUALSCHEMANAME=default&ATTRIBUTES=hsapiens_gene_ensembl.default.feature_page.ensembl_gene_id|hsapiens_gene_ensembl.default.feature_page.ensembl_transcript_id&FILTERS=hsapiens_gene_ensembl.default.filters.with_hgnc.only|hsapiens_gene_ensembl.default.filters.biotype."protein_coding"&VISIBLEPANEL=filterpanel`

3. How many genes have an orthologue in mouse? Use the homologue filter. 

    17,776 (Note: Question does not ask about protein coding genes)

    `http://www.ensembl.org/biomart/martview/8be1315d1dc4c168ad490a24632760ad?VIRTUALSCHEMANAME=default&ATTRIBUTES=hsapiens_gene_ensembl.default.feature_page.ensembl_gene_id|hsapiens_gene_ensembl.default.feature_page.ensembl_transcript_id&FILTERS=hsapiens_gene_ensembl.default.filters.with_hgnc.only|hsapiens_gene_ensembl.default.filters.biotype."protein_coding"|hsapiens_gene_ensembl.default.filters.with_mmusculus_homolog.only&VISIBLEPANEL=resultspanel`

4. In what basic formats can you download your results?

### Retrieving Results

1. In what basic formats can you download your results?

    TSV, CSV, HTML, XLS

2. Figure out and explain what the top buttons, labeled "URL", "XML", and "Perl", are for.

    They are for exporting your query to a URL, XML document, or Perl script. This lets you programmatically reconstruct a query created using the web interface.

### Downloading sequences

Restrict your gene set to contain only those genes coding for proteins containing a domain with the Pfam identifier PF00104. This should give you 53 genes.

`http://www.ensembl.org/biomart/martview/5e316c9abadb04c4bd20ce62dc893300?VIRTUALSCHEMANAME=default&ATTRIBUTES=hsapiens_gene_ensembl.default.feature_page.ensembl_gene_id|hsapiens_gene_ensembl.default.feature_page.ensembl_transcript_id&FILTERS=hsapiens_gene_ensembl.default.filters.biotype."protein_coding"|hsapiens_gene_ensembl.default.filters.pfam."PF00104"&VISIBLEPANEL=filterpanel`

1. What sequence format is used for downloading sequences?

    FASTA

2. In the "attributes" settings, you can choose what kind of sequences you download. What is the difference between "unspliced transcript" and "unspliced gene"?

    Unspliced transcript is the full unspliced transcript with exons and introns.

    Unspliced gene gives the exons and introns of a gene

3. What is the difference between "unspliced transcript" and "cDNA"?

    Unspliced transcript is the transcript with exons and introns.

    cDNA (complementary dna) is derived from mRNA so it does not contain introns. cDNA is an mRNA's transcript sequence expressed as DNA bases rather than RNA (replace uracil with thymine)

4. Suppose you want to work with genes' coding regions. If you download the "coding sequence" for your 53 genes, how many sequences do you get? Explain the discrepancy.

    I see 230 sequences in the FASTA file. These sequences are the coding regions of the genes with the introns spliced out. A gene may produce alternative transcripts and that could be a possible reason.

## Querying Ensembl

1. How many databases are available for cat, felis catus?

```
mysql -u anonymous -h ensembldb.ensembl.org -P 3306
show databases like 'felis_catus%'
```

119

2.  Use the show and describe commands to figure what tables are related to describing genes, transcripts, and exons. What information are these tables storing and how do the tables relate to each other?

```
mysql -u anonymous -h ensembldb.ensembl.org -P 3306 homo_sapiens_core_90_38
show tables;
describe exon;
describe transcript;
describe gene;
describe exon_transcript;
```
Gene and exon can be joined with `sequence_region_id` to the `seq_region` table. Genes and transcripts can be joined together as the transcript table contains a `gene_id` column. The join table `exon_transcript` allows exons and transcripts to be joined.

3.  How many genes are registred for human? Make a breakdown based on the column "biotype" by using the GROUP BY directive.

```
SELECT biotype, COUNT(*) AS count FROM gene GROUP BY biotype ORDER BY COUNT(*) DESC;
```

4. How many processed pseudogenes have a non-empty description string? 

```
mysql> SELECT biotype, COUNT(*) AS count FROM gene WHERE biotype = 'processed_pseudogene' AND description > '' GROUP BY biotype;
+----------------------+-------+
| biotype              | count |
+----------------------+-------+
| processed_pseudogene |  5283 |
+----------------------+-------+
1 row in set (0,05 sec)
```

5. How many transcripts are associated with the two breast-cancer associated genes BRCA1 (ENSG00000012048) and BRCA2 (ENSG00000139618)? Your solution is supposed to be written as one SQL query. 

```
mysql> SELECT COUNT(*) FROM transcript JOIN gene ON gene.gene_id = transcript.gene_id WHERE gene.stable_id = 'ENSG00000012048' OR gene.stable_id = 'ENSG00000139618';
+----------+
| COUNT(*) |
+----------+
|       37 |
+----------+
1 row in set (0,04 sec)
```

## Interfacing to SQLite from Python

    No notes. Run the script db_query.py and explain the output

    https://kth.instructure.com/courses/3845/assignments/16734?module_item_id=49109