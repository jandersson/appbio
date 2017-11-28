class SequenceReader:
    def __init__(self):
        self.data = None
        self.filename = None
        self.sequences = dict()

    def read_file(self, filename):
        self.data = None
        with open(filename, 'r') as f:
            self.data = f.readlines()
        self.read_sequences()
    
    def read(self, data):
        self.data = None
        self.data = data.splitlines()
        self.read_sequences()
    
    def read_sequences(self):
        raise NotImplementedError

    def print_sequence_names(self):
        """Print out the list of sequences and the number of sequences"""
        print(len(self.sequences))
        for sequence in self.sequences:
            print(sequence)