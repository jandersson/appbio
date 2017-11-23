def to_fasta(name, sequence, max_width=60):
    """Format a DNA sequence string in FASTA"""
    fasta_sequence = ""
    fasta_sequence += f">{name}\n"
    fasta_sequence += "\n".join([sequence[index : index + max_width] for index in range(0, len(sequence), max_width)])
    return fasta_sequence