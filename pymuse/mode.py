from . import scale
from .scale import Scale
from .notation import *

class Mode(Scale):
    """ A mode is a scale which has its fundamental at a different degree
        The mode keeps the notes of the scale
    """

    def __init__(self, fundamental, degree, intervals=scale.INTERVALS[scale.MAJOR]):
        Scale.__init__(self, fundamental, intervals)
        self.degree = degree
        self.fundamental = self.fundamental + self[degree]
        self._intervals = self._intervals[degree:] + self._intervals[:degree]

    def __str__(self):
        string = Scale.__str__(self)
        if self.degree == 1:
            string += ' ionian'
        elif self.degree == 2:
            string += ' dorian'
        elif self.degree == 3:
            string += ' phrygian'
        elif self.degree == 4:
            string += ' lydian'
        elif self.degree == 5:
            string += ' myxolidian'
        elif self.degree == 6:
            string += ' aeolian'
        if self.degree == 7:
            string += ' locrian'
        return string
