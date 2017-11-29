from sequence_reader import SequenceReader

class FastaReader(SequenceReader):
    def is_sequence_name_line(self, line):
        return line[0] == '>'

    def get_sequence_name(self, line):
        if not self.is_sequence_name_line(line): 
            return 
    
        return line[1:].rstrip()
    
    def get_sequence(self, line):
        return line.rstrip()

    def read_sequences(self):
        for line in self.data:
            if self.is_sequence_name_line(line):
                sequence = ""
                name = self.get_sequence_name(line)
                self.sequences[name] = sequence
            else:
                self.sequences[name] += self.get_sequence(line)

if __name__ == '__main__':
    import os
    reader = FastaReader()
    data_path = os.path.join(os.path.dirname(__file__), os.pardir, 'data')
    test_files = ['an_exon.fa']
    for data_file in test_files:
        data = os.path.join(data_path, data_file)
        reader.read_file(data)        
        reader.print_sequence_names()
        print(reader.sequences)