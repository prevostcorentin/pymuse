from ..pymuse import Scale, INTERVALS, MINOR
from ..pymuse.notation import *


def test_getitem():
    for n in range(12):
        scale = Scale(n)
        for octave in range(3):
            for i, pitch in enumerate([p + (12 * octave) for p in scale[:7]]):
                assert scale[i + octave * 7] == pitch

def test_getitem_first_octave_sliced():
    scale = Scale(0)
    assert scale[I:IIX] == [C, D, E, F, G, A, B]

def test_getitem_second_octave_sliced():
    scale = Scale(0)
    assert scale[IIX:IIX + IIX] == [C2, D2, E2, F2, G2, A2, B2]

def test_getitem_third_octave_sliced():
    scale = Scale(0)
    assert scale[IIX + IIX:IIX + IIX + IIX] == [C3, D3, E3, F3, G3, A3, B3]

def test_relative_scale():
    c_major_scale = Scale(0)
    a_minor_scale = Scale(9, INTERVALS[MINOR])
    assert c_major_scale.relative[:] == [9, 11, 12, 14, 16, 17, 19]
    assert a_minor_scale.relative[:] == [0, 2, 4, 5, 7, 9, 11]
