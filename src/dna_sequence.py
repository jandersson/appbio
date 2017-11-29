class DnaSequence(object):
    def __init__(self, sequence=''):
        self.sequence = sequence

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, new_sequence):
        self._sequence = new_sequence.upper().strip()
        self._compute_gc()

    def _compute_gc(self): 
        if self._sequence == "":
            self.gc_content = 0
        else:
            seq = self._sequence
            cytosine_count = seq.count('C')
            guanine_count = seq.count('G')
            adanine_count = seq.count('A')
            thymine_count = seq.count('T')
            self.gc_content = (guanine_count + cytosine_count) / (cytosine_count + guanine_count + adanine_count + thymine_count)

    def __repr__(self):
        return self._sequence

if __name__ == '__main__':
    s = DnaSequence()
    s.sequence = 'GATTACA'
    print(s)
    print(s.gc_content)
    s = DnaSequence('GCAT')
    print(s.sequence)
    print(s.gc_content)