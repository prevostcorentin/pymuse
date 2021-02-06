""" Class that represents a Scale"""

from .note import Note
from .scale import Scale
from .notation import *


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
        return str(representation)

    def __str__(self):
        notation = Note(self[0]).notation
        if self.is_major:
            notation = notation + ' M'
        else:
            notation = notation + ' m'
        return notation

    @property
    def is_major(self):
        first_note = self.__getitem__(0)
        for remaining_note in self[1:]:
            if remaining_note - first_note == 4:
                return True
            elif remaining_note - first_note == 3:
                return False
        return False