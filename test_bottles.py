from collections import namedtuple
from textwrap import dedent


class BottleCount(namedtuple('_bottlecount', 'value')):

    def __str__(self):
        if self.value == 0:
            return "No more bottles of beer"
        elif self.value == 1:
            return "1 bottle of beer"

        return f"{self.value} bottles of beer"


def BottleCounter(start, end):

    for current in range(start, end - 1, -1):
        next_ = 99 if current == 0 else current - 1
        yield BottleCount(current), BottleCount(next_)


class Verse:

    def __init__(self, current, next_):
        self.current = current
        self.next = next_

    def matches(self):
        return self.current.value > 0

    def sing(self):
        return (f"{self.current} on the wall\n"
                f"{self.current}\n"
                f"{self.action}\n"
                f"{self.next} on the wall\n"
               )

    @property
    def action(self):
        return ("Take one down\n"
                "Pass it around")


class FinalVerse(Verse):

    def __init__(self, current, next_):
        self.current = current
        self.next = next_

    def matches(self):
        return self.current.value == 0

    @property
    def action(self):
        return ("Go to the store\n"
                "Buy some more")


class BottleSong:

    _verses = [
        Verse,
        FinalVerse
    ]

    def sing(self, current, next_):
        for v in self._verses:
            verse = v(current, next_)
            if verse.matches():
                return verse.sing()

    def verse(self, num):
        return self.verses(num, num)

    def verses(self, start, end=0):
        counter = BottleCounter(start, end)
        return "\n".join(
            self.sing(current, next_)
            for current, next_ in counter)


def clean(s):
    return dedent(s.lstrip('\n'))

def test_first_verse():
    song = BottleSong()
    assert song.verse(99) == clean("""
        99 bottles of beer on the wall
        99 bottles of beer
        Take one down
        Pass it around
        98 bottles of beer on the wall
    """)


def test_another_verse():
    song = BottleSong()
    assert song.verse(3) == clean("""
        3 bottles of beer on the wall
        3 bottles of beer
        Take one down
        Pass it around
        2 bottles of beer on the wall
    """)


def test_next_to_penultimate_verse():
    song = BottleSong()
    assert song.verse(2) == clean("""
        2 bottles of beer on the wall
        2 bottles of beer
        Take one down
        Pass it around
        1 bottle of beer on the wall
    """)


def test_penultimate_verse():
    song = BottleSong()
    assert song.verse(1) == clean("""
        1 bottle of beer on the wall
        1 bottle of beer
        Take one down
        Pass it around
        No more bottles of beer on the wall
    """)

def test_final_verse():
    song = BottleSong()
    assert song.verse(0) == clean("""
        No more bottles of beer on the wall
        No more bottles of beer
        Go to the store
        Buy some more
        99 bottles of beer on the wall
    """)

def test_a_couple_of_verses():
    song = BottleSong()
    assert song.verses(99, 98) == clean("""
        99 bottles of beer on the wall
        99 bottles of beer
        Take one down
        Pass it around
        98 bottles of beer on the wall

        98 bottles of beer on the wall
        98 bottles of beer
        Take one down
        Pass it around
        97 bottles of beer on the wall
    """)
