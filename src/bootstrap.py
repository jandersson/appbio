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

    from common import is_valid_file
    from fasta_reader import FastaReader
    from fasta_writer import to_fasta

    parser = argparse.ArgumentParser(description='Run Phylip bootstrap analysis on protein alignments')
    parser.add_argument('file', type=lambda f: is_valid_file(f, parser),
                        help='Protein alignment file in FASTA format')
    parser.add_argument('num_replicates', help='Number of bootstrap replicates to run')
    args = parser.parse_args(['/home/jonas/appbio/data/small1.fa', '1000'])

    reader = FastaReader()
    reader.read_file(args.file)
    seq_string = to_seqboot(reader.sequences)
    infile = tempfile.NamedTemporaryFile()
    infile.write(seq_string.encode())
    infile.seek(0)

    seqboot = pexpect.spawn('seqboot', encoding='utf-8')
    seqboot.expect(str('Please enter a new file name'))
    seqboot.sendline(infile.name)
    seqboot.expect('Y to accept')
    seqboot.sendline("I")
    seqboot.sendline("R")
    seqboot.expect('Number of replicates')
    seqboot.sendline("1000")
    seqboot.expect('Y to accept')
    seqboot.sendline('Y')
    seqboot.expect('Random number seed')
    seqboot.sendline('1001')
    i = seqboot.expect([pexpect.EOF, 'please type R, A, F, or Q'])
    if i == 1:
        seqboot.sendline("R")
    infile.close()
    
