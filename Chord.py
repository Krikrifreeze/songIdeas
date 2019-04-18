class Chord:
    def __init__(self, num, q, octa):
        self.number = num #number 1 - 7 based on nashvile number systemS
        self.quality = q #maj, min, aug, dim, maj7, 
        self.octave = octa
    def __repr__(self):
        return str(self.number)