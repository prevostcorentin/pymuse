import pymuse
from pymuse import Note


C_SCALE = set([0, 2, 4, 5, 7, 9, 11])


def test_pitch_to_degree():
    """ Test for 24*2 octaves that pitch is expected from degree in c scale """
    for octave in range(24):
        for pitch in range(12):
            assert Note(pitch + octave*12).degree == pitch + 1


def test_notation():
    for octave in range(24):
        for degree, pitch in enumerate(C_SCALE):
            assert Note(pitch + octave*12).notation == 'CDEFGAB'[degree]
        for degree, pitch in C_SCALE.difference(set(range(12))):
            notation = ['C#', 'D#', 'F#', 'G#', 'A#'][degree]
            assert Note(pitch + octave*12).notation == notation


def test_alteration():
    for octave in range(24):
        for pitch in C_SCALE:
            assert not Note(pitch + octave*12).alteration
        for pitch in C_SCALE.difference(set(range(12))):
            assert Note(pitch + octave*12).alteration
