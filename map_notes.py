import os
import json
from itertools import takewhile, count


NOTES_NAME = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]


# NOTE: start_frequency here is a C2
def note_map(start_frequency=65.40639, start_octave=2, end_octave=7):
    freq_map = dict()
    for i in range(start_octave, 1 + end_octave):
        for j in range(0, 12):
            freq_map[f"{NOTES_NAME[j]}{i}"] = start_frequency * pow(2, (((i - start_octave) * 12) + j) / 12)
    return freq_map


def create_note_map():
    os.makedirs("data", exist_ok=True)
    with open("data/note_map.json", "w") as f:
        f.write(json.dumps(note_map(), indent=4))


# Maps a given frequency to the closest note on the note map
def get_closest_note(frequency):
    note_dict = note_map()
    closest_note = min(note_dict .values(), key=lambda x: abs(x - frequency))

    return list(note_dict.keys())[list(note_dict .values()).index(closest_note)]



# Return the harmonic series from a given freuency as a dicitonary,
# where the key is the scientific pitch notation and the value is the corresponding pitch
def harmonic_series(frequency, threshold=None):
    # Sets the threshold to the last note in the note_map if unspecified
    if threshold is None:
        threshold = note_map(start_octave=2, end_octave=7)["B7"]
     
    # Basically a while loop that terminates when the threshold is passed
    return { get_closest_note(val) : val for val in takewhile(lambda x: x < threshold, (note_map()[get_closest_note(frequency)] * pow(2, i) for i in count())) }


