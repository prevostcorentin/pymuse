#! pymuse-venv/bin/python
# coding: utf-8
import click
import pymuse


@click.group(invoke_without_command=True)
@click.option('--pitch', required=True, type=int,
              help='Beginning pitch')
@click.option('--degree', type=int, default=0,
              help='Display mode from degree')
@click.option('--seventh/--no-seventh', default=False,
              help='Add seventh to chords')
@click.option('--sixth/--no-sixth', default=False,
              help='Add sixth to chords')
@click.option('--fourth/--no-fourth', default=False,
              help='Add fourth to chords')
@click.option('--display-pitches/--no-display-pitches', default=False)
@click.option('--display-notation/--no-display-notation', default=True)
@click.option('--show-intervals/--no-show-intervals', default=False,
              help='Show semi-tons between degrees')
def cli(pitch, degree, fourth, sixth, seventh, display_pitches, display_notation, show_intervals):
    """ Display informations from pymuse as readable format """
    scale = pymuse.Mode(pitch, degree)
    formatted = {'degrees': '', 'pitches': ''}
    for n, _  in enumerate(scale):
        intervals = [0, 2, 4]
        if fourth:
            intervals = intervals + [3]
        if sixth:
            intervals = intervals + [5]
        if seventh:
            intervals = intervals + [6]
        chord = pymuse.Chord(scale, [d + n for d in intervals])
        if display_notation:
            formatted['degrees'] += '{:12}'.format(chord)
        if display_pitches:
            notes = []
            for pitch in chord:
                formatted['pitches'] += '{:} '.format(pitch)
            formatted['pitches'] += '   '
    print(scale)
    for s in formatted:
        if formatted[s]:
            print(formatted[s])
    if show_intervals:
        s = ''
        for i in range(1, scale.size + 1):
            s += '+{:<12}'.format(str(abs(scale[i-1] - scale[i])) + ' ½t')
        print(s)

if __name__ == '__main__':
    cli(obj={})
