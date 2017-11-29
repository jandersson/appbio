class DnaSequence(object):
    def __init__(self, sequence=""):
        self._sequence = sequence

    @property
    def sequence(self):
        return self._sequence

    def sequence(self, new_sequence):
        self._sequence = new_sequence
        self.compute_gc()

    def compute_gc(self): 
        pass