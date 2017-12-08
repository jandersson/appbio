def to_seqboot(sequences):
    length = len([value.sequence for value in sequences.values()][0])
    seq_string = ""
    seq_string += f"{len(sequences):5}    {length}\n"
    for name, sequence in sequences.items():
        seq_string += f"{name:10}{sequence}\n"
    return seq_string

if __name__ == '__main__':
    import argparse
    import tempfile
    import pexpect
    import os
    from Bio import AlignIO
    from common import is_valid_file
    from fasta_reader import FastaReader
    from fasta_writer import to_fasta

    parser = argparse.ArgumentParser(description='Run Phylip bootstrap analysis on protein alignments')
    parser.add_argument('file', type=lambda f: is_valid_file(f, parser),
                        help='Protein alignment file in FASTA format')
    parser.add_argument('num_replicates', help='Number of bootstrap replicates to run')
    args = parser.parse_args()

    alignment = AlignIO.read(args.file, 'fasta')
    infile = tempfile.NamedTemporaryFile(mode='w+t')
    AlignIO.write(alignment, infile, 'phylip')
    infile.seek(0)

    seqboot = pexpect.spawn('seqboot', encoding='utf-8')
    seqboot.expect(str('Please enter a new file name'))
    seqboot.sendline(infile.name)
    seqboot.expect('Y to accept')
    seqboot.sendline("R")
    seqboot.expect('Number of replicates')
    seqboot.sendline(args.num_replicates)
    seqboot.expect('Y to accept')
    seqboot.sendline('Y')
    seqboot.expect('Random number seed')
    seqboot.sendline('1001')
    if seqboot.expect([pexpect.EOF, 'please type R, A, F, or Q']) == 1:
        seqboot.sendline("R")
    infile.close()
    os.rename('outfile', 'infile')
    
    protdist = pexpect.spawn('protdist', encoding='utf-8', timeout=60)
    protdist.expect('Are these settings correct')
    protdist.sendline('2')
    protdist.sendline("M")
    protdist.expect('type D or W')
    protdist.sendline('D')
    protdist.expect('How many data sets')
    protdist.sendline(args.num_replicates)
    protdist.expect('Are these settings correct')
    protdist.sendline('Y')
    protdist.expect(pexpect.EOF)
    os.rename('outfile', 'infile')

    neighbor = pexpect.spawn('neighbor', encoding='utf-8')
    neighbor.expect('Y to accept')
    neighbor.sendline('2')
    neighbor.sendline('M')
    neighbor.expect('How many data sets')
    neighbor.sendline(args.num_replicates)
    neighbor.expect('Random number seed')
    neighbor.sendline('1001')
    neighbor.expect('Y to accept')
    neighbor.sendline('Y')
    neighbor.expect(pexpect.EOF)
    os.rename('outtree', 'intree')
    os.rename('outfile', 'infile')

    consense = pexpect.spawn('consense', encoding='utf-8')
    consense.expect('Are these settings correct')
    consense.sendline('2')
    consense.sendline('Y')
    consense.expect(pexpect.EOF)
    os.remove('infile')
    os.remove('intree')
    os.remove('outfile')

    with open('outtree', 'r') as f:
        for line in f:
            print(line, end='')

    os.remove('outtree')