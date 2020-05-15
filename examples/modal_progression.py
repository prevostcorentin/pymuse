from pymuse.chord import Chord
from pymuse.mode import Mode
from pymuse.note import Note
from random import randint


if __name__ == '__main__':
    mode = Mode([0, 2, 4, 5, 7, 9, 11][randint(0, 6)], degree=randint(0, 6))
    print(mode, '\n')
    progression = [i + randint(1, 3) for i in range(randint(4, 8))]
    chords = []
    for degree in [0] + progression:
        chords.append(Chord(mode, [degree,
                                   degree + 2 + randint(0, 1),
                                   degree + 4 + randint(0, 1)]))
    for chord in chords:
        string = '   '
        for pitch in chord.pitches:
            string = string + Note(pitch).notation + '   '
        print(chord)
        print(string)


if __name__ == '__main__':
    random_modal_progression()
