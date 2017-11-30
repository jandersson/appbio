class DnaSequence(object):
    def __init__(self, sequence=''):
        self.sequence = sequence
        self._gc_content = 0

    @property
    def c_count(self):
        return self.sequence.count('C')

    @property
    def a_count(self):
        return self.sequence.count('A')
    
    @property
    def t_count(self):
        return self.sequence.count('T')

    @property
    def g_count(self):
        return self.sequence.count('G')

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, new_sequence):
        self._sequence = new_sequence.upper().strip()

    @property
    def gc_content(self):
        self._compute_gc()
        return self._gc_content

    def _compute_gc(self): 
        if self._sequence == "":
            self._gc_content = 0
        else:
            cytosine_count = self.c_count
            guanine_count = self.g_count
            adanine_count = self.a_count
            thymine_count = self.t_count
            try:
                self._gc_content = (guanine_count + cytosine_count) / (cytosine_count + guanine_count + adanine_count + thymine_count)
            except ZeroDivisionError:
                self._gc_content = 0
    def __repr__(self):
        return self.sequence

    def diff(self, other_sequence):
        """Compute the composition difference using root-mean-square"""
        

if __name__ == '__main__':
    s = DnaSequence()
    s.sequence = 'GATTACA'
    print(s)
    print(s.gc_content)
    s = DnaSequence('GCAT')
    print(s.sequence)
    print(s.gc_content)