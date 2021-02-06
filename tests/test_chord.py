from ..pymuse import Chord, Scale
from ..pymuse.notation import *


def test_c_ionian_perfect_chord():
    chord = Chord(Scale(0), definition=[I, III, V])
    assert chord[:] == [0, 4, 7]
    assert len(chord[:]) == 3

def test_c_ionian_seventh_chord():
    chord = Chord(Scale(0), definition=[I, III, V, VII])
    assert chord[:] == [0, 4, 7, 11]
    assert len(chord[:]) == 4

def test_e_ionian_seventh_chord():
    chord = Chord(Scale(5), definition=[I, III, V, VII])
    assert chord[:] == [5, 9, 12, 16]
    assert len(chord[:]) == 4

def test_c_ionian_perfect_superior_octave():
    chord = Chord(Scale(0), definition=[IIX, III + IIX, V + IIX])
    assert chord[:] == [12, 16, 19]
    assert len(chord[:]) == 3

def test_is_major():
    c_major = Chord(Scale(0), definition=[I, III, V])
    assert c_major.is_major

def test_is_minor():
    d_minor = Chord(Scale(0), definition=[II, IV, VI])
    assert not d_minor.is_major

def test_c_major_notation():
    assert str(Chord(Scale(0), definition=[I, III, V])) == "C M"

def test_d_minor_notation():
    assert str(Chord(Scale(0), definition=[II, IV, VI])) == "D m"

def test_d_sharp_myxolydian_notation():
    assert str(Chord(Scale(4), definition=[V, VII, IX, XII])) == "D# 7"

def test_c_mixolydian_notation():
    assert str(Chord(Scale(0), [4, 6, 8, 10])) == 'G 7'

def test_locrian_notation():
    """ Test locrian chord notation in C major scale """
    # Locrian chord
    assert str(Chord(Scale(0), [6, 8, 10, 12])) == 'B m7b5'