from ..pymuse import Mode
from ..pymuse.notation import *

C_SCALE = [0, 2, 4, 5, 7, 9, 11]


def transpose(scale, degree):
    """ Get the mode of a scale """
    return scale[degree:] + [d + 12 for d in scale[:degree]]


def test_getitem():
    """ Modes of C scale """
    for degree in range(0, 7):
        mode = Mode(0, degree)
        expected_mode = transpose(C_SCALE, degree)
        for i in range(0, 7):
            assert mode[i] == expected_mode[i]


def test_zero_mode_is_one():
    """ Mode(0, 0) must be ionian """
    assert Mode(0, I)[:] == [0, 2, 4, 5, 7, 9, 11]
