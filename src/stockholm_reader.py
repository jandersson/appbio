from sequence_reader import SequenceReader

class StockholmReader(SequenceReader):

    def read_sequences(self):
        """Populate the sequences dictionary in the given input file"""
        for line in self.data:
            if not self.is_sequence_line(line):
                continue
            if not line.strip():
                continue
            name = line.expandtabs().split()[0]
            try:
                sequence = line.expandtabs().split()[1]
            except IndexError:
                sequence = ""
            self.sequences[name] = sequence

    def is_sequence_line(self, line):
        """"Check if a line contains a sequence"""
        if line[0] == '#':
            return False
        if line[0].replace('/', '') == "":
            return False
        return True

if __name__ == '__main__':
    import os
    data_path = os.path.join(os.path.dirname(__file__), os.pardir, 'data')
    test_files = ['shortseqs.sthlm', 'longseqs.sthlm', 'cornercase.sthlm']
    for data_file in test_files:
        reader = StockholmReader()
        data = os.path.join(data_path, data_file)
        reader.read_file(data)        
        reader.print_sequence_names()