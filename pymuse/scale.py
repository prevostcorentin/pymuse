""" Class that represents a scale """

from .note import Note


MAJOR = 0
MINOR = 1

INTERVALS = {
    MAJOR: [2, 2, 1, 2, 2, 2, 1],
    MINOR: [2, 1, 2, 2, 1, 2, 2],
}


class Scale(object):


    def __init__(self, fundamental, intervals=INTERVALS[MAJOR]):
        self.fundamental = fundamental % 12
        # if only the same interval
        if set(intervals).union(set(intervals)) == set([intervals[0]]):
            self._intervals = [intervals[0]]
        else:
            self._intervals = intervals

    @property
    def relative(self):
        """ Get the relative scale  """
        if self._intervals == INTERVALS[MAJOR]:
            offset = 5
        elif self._intervals == INTERVALS[MINOR]:
            offset = 2
        return Scale(self[offset], self._intervals[offset:] +
                                   self._intervals[:offset])

    def __contains__(self, what):
        degrees = [d % 12 for d in self[:len(self)]]
        for p in what[:]:
            if p % 12 not in degrees:
                return False
        return True

    def __getitem__(self, item):
        if isinstance(item, slice):
            start, stop, step = item.start, item.stop, item.step
            if start is None:
                start = 0
            if stop is None:
                stop = len(self)
            if step is None:
                step = 1
            return [self[i] for i in range(start, stop, step)]
        pitch = self.fundamental
        for i in range(min(item, 0), max(item, 0)):
            pitch = pitch + self._intervals[i % len(self._intervals)]
        return pitch

    def __eq__(self, other):
        return other.intervals == self._intervals and \
               other.fundamental == self.fundamental % 12

    def __repr__(self):
        return 'fundamental: {}\tintervals: {}'.format(self.fundamental,
                                                       str(self._intervals))

    def __len__(self):
        return len(self._intervals)

    def __str__(self):
        string = Note(self.fundamental).notation
        if len(self._intervals) == 1:
            if self._intervals == [3]:
                return string + ' diminished'
            elif self._intervals == [2]:
                return string + ' tone per tone'
            elif self._intervals == [1]:
                return string + ' chromatic'
        for n in range(1, len(self.degrees) + 1):
            interval = (self[n] - self.fundamental) % 12
            if interval == 3:
                string += 'm'
        return string
