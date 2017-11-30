from sequence_reader import SequenceReader
from dna_sequence import DnaSequence


class FastaReader(SequenceReader):
    def is_sequence_name_line(self, line):
        return line[0] == '>'

    def get_sequence_name(self, line):
        """If the line is a sequence name, process and return"""
        if not self.is_sequence_name_line(line):
            return
        
        return line.split()[0].rstrip()[1:]

    def get_sequence(self, line):
        """Process sequence line and return it"""
        return line.rstrip()

    def read_sequences(self):
        for line in self.data:
            if self.is_sequence_name_line(line):
                sequence = DnaSequence()
                name = self.get_sequence_name(line)
                self.sequences[name] = sequence
            else:
                self.sequences[name].sequence += self.get_sequence(line)

if __name__ == '__main__':
    import os
    data_path = os.path.join(os.path.dirname(__file__), os.pardir, 'data')
    test_files = ['an_exon.fa', 'translationtest.dna']
    for data_file in test_files:
        reader = FastaReader()
        data = os.path.join(data_path, data_file)
        reader.read_file(data)
        reader.print_sequence_names()
        print(reader.sequences)
