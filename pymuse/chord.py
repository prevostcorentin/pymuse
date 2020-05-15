""" Class that represents a Note """

from .note import Note
from .scale import Scale
from .notation import *

from functools import reduce

class Chord(Scale):

    def __init__(self, scale, definition):
        self._intervals = []
        self.fundamental = scale[definition[0]]
        last_degree = 0
        for degree in definition[1:]:
            interval = 0
            degree = degree % len(scale._intervals)
            for i in range(last_degree, degree):
                interval += scale._intervals[i]
            last_degree = degree
            self._intervals.append(interval)

    def __len__(self):
        return len(self._intervals) + 1

    def __repr__(self):
        representation = [Note(pitch) for pitch in self[:]]
        return representation

    def __str__(self):
        return Note(self[0]).notation
