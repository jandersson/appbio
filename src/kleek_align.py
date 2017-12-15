if __name__ == '__main__':
    import re
    from Bio import SeqIO
    from common import file_parser
    import tempfile
    import os
    import subprocess

    parser = file_parser(prog_desc='Run KLEEKs through muscle and view with seaview', file_desc='A FASTA file containing protein sequences')
    args = parser.parse_args()

    working_dir = tempfile.TemporaryDirectory()
    os.chdir(working_dir.name)
    kleek_filter = re.compile(r'KL[EI]{2,}K')
    kleeks = []
    with open(args.file, 'rU') as fd:
        for record in SeqIO.parse(fd, 'fasta'):
            if re.search(kleek_filter, str(record.seq)):
                kleeks.append(record)
    kleek_file = tempfile.NamedTemporaryFile(mode='w+t')
    SeqIO.write(kleeks, kleek_file, 'fasta')
    kleek_file.seek(0)
    subprocess.run(['/home/jonas/opt/muscle', '-in', f"{kleek_file.name}", '-fastaout', f"{working_dir.name}" + 'outfile.fa'])
    subprocess.run(['/home/jonas/opt/seaview/seaview', f"{working_dir.name}" + 'outfile.fa'])

    
