import pymuse
from pymuse.note import Note
from pymuse.chord import Chord
from pymuse.scale import Scale

from random import randint


def random_progression(chords=4):
    scale = Scale(randint(0, 11))
    print('Scale tone:', scale)
    for n in range(chords):
        degrees = []
        for i in range(randint(2, 5)):
            degrees.append([0, 2, 4][i-2] + n + randint(1, 7))
        print(Chord(scale, degrees))

if __name__ == '__main__':
     random_progression()
