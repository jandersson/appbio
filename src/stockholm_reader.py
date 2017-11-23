class StockholmReader:
    def __init__(self):
        self.data = None
        self.filename = None
        self.sequences = dict()

    def read_file(self, filename):
        self.data = None
        with open(filename, 'r') as f:
            self.data = f.readlines()
        if not self.data:
            raise Exception
        self.read_sequences()
    
    def read(self, data):
        self.data = None
        self.data = data.splitlines()
        self.read_sequences()

    def read_sequences(self):
        """Populate the sequences dictionary in the given input file"""
        for line in self.data:
            if not self.is_sequence_line(line):
                continue
            if not line.strip():
                continue
            name = line.split('\t')[0]
            sequence = line.rsplit('\t', maxsplit=1)[1].strip('\n')
            self.sequences[name] = sequence

    def print_sequence_names(self):
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
    reader = StockholmReader()
    data_path = '/home/jonas/appbio/data/'
    test_files = ['shortseqs.sthlm', 'longseqs.sthlm', 'cornercase.sthlm']
    for data_file in test_files:
        data = os.path.join(data_path, data_file)
        reader.read_file(data)        
        reader.print_sequence_names()