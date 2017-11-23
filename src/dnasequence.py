def to_fasta(name, sequence, max_width=60):
    """Format a DNA sequence string in FASTA"""
    fasta_sequence = ""
    fasta_sequence += f">{name}\n"
    fasta_sequence += "\n".join([sequence[index : index + max_width] for index in range(0, len(sequence), max_width)])
    return fasta_sequence

if __name__ == '__main__':
    from stockholm_reader import StockholmReader
    reader = StockholmReader()
    test_string = """# STOCKHOLM 1.0 
prot17                 MAGQDPRLRGEPLKHVLVIDDDVAMRHLIVEYLTIHAFKVTAVADSKQFNRVLCSETVDVVVV
prot4711\t\tAAGQDVRLRGEPL----VIDDDVAMRHLIVEYLTIDAFKVTAVADSKQFNRVLCSETVDVVVV
//"""
    reader.read(test_string)
    print(reader.sequences)
