class StockholmReader:
    def __init__(self, filename):
        self.filename = filename
        with open(filename, 'r') as f:
            self.data = f.readlines()
        if not self.data:
            raise Exception
        
        self.read_sequences()
        self.print_sequences()

    def read_sequences(self):
        """Populate the sequences list in the given input file"""
        self.sequences = []
        for line in self.data:
            if not self.is_sequence_line(line):
                continue
            if not line.strip():
                continue
            self.sequences += [line.split()[0]]

    def print_sequences(self):
        """Print out the list of sequences and the number of sequences"""
        print(len(self.sequences))
        for sequence in self.sequences:
            print(sequence)

    def is_sequence_line(self, line):
        """"Check if a line contains a sequence"""
        if line[0] == '#':
            return False
        if line[0].replace('/', '') == "":
            return False
        return True

if __name__ == '__main__':
    import os
    data_path = '/home/jonas/appbio/data/'
    test_files = ['shortseqs.sthlm', 'longseqs.sthlm', 'cornercase.sthlm']
    for data_file in test_files:
        data = os.path.join(data_path, data_file)
        reader = StockholmReader(data)        