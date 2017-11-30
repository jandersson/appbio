from math import sqrt

class DnaSequence(object):
    def __init__(self, sequence=''):
        self.sequence = sequence
        self._gc_content = 0

    def __repr__(self):
        return self.sequence

    def __str__(self):
        return self.sequence 

    def __sub__(self, other):
        return self.diff(other)

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
    def a_ratio(self):
        return (self.a_count) / (self.a_count + self.g_count + self.c_count + self.t_count)

    @property
    def c_ratio(self):
        return (self.c_count) / (self.a_count + self.g_count + self.c_count + self.t_count)

    @property
    def g_ratio(self):
        return (self.g_count) / (self.a_count + self.g_count + self.c_count + self.t_count)

    @property
    def t_ratio(self):
        return (self.t_count) / (self.a_count + self.g_count + self.c_count + self.t_count) 

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

    def diff(self, other_sequence):
        """Compute the composition difference using root-mean-square"""
        numerator = ((self.a_ratio - other_sequence.a_ratio) ** 2) + ((self.c_ratio - other_sequence.c_ratio) ** 2) + ((self.g_ratio - other_sequence.g_ratio) ** 2) + ((self.t_ratio - other_sequence.t_ratio) ** 2)
        numerator = numerator * 0.25
        return sqrt(numerator)

if __name__ == '__main__':
    s = DnaSequence()
    s.sequence = 'GATTACA'
    print(s)
    print(s.gc_content)
    s = DnaSequence('GCAT')
    print(s.sequence)
    print(s.gc_content)
    print(s.diff(DnaSequence('GCAT')))
    print(s.diff(DnaSequence('GATTACA')))
    print(s - DnaSequence('GCAT'))
    print(DnaSequence('GCAT') - s)