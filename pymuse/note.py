import math
from math import ceil


class Note(object):
    """ Class that represents a note by its MIDI pitch """

    def __init__(self, pitch):
        self.degree = pitch % 12 + 1

    @property
    def notation(self):
        """ Get the name of the note from the alphabet """
        C_SCALE = 'CDEFGAB'
        index = int(ceil(self.degree - self.degree/2))
        if self.degree % 2 and self.degree < 6:
            index = index - 1
        if self.alteration:
            return C_SCALE[index - 1] + '#'
        return C_SCALE[index]

    @property
    def alteration(self):
        """ Return True if the note is altered (sharp or flat)
         1 2    3 4    5      6 | 7    8 9      10 11   12
         C C#   D D#   E      F | F#   G G#     A  A#   B
                       ^        |                       ^
                       |        |                       |
                  Not altered   |                  Not altered

        The altered note in the left part of the split is odd
        In the right part, the altered is even
        """
        if self.degree == 6 or (self.degree % 7) % 2:
            return 0
        else:
            return 1

    def __str__(self):
        return self.notation
