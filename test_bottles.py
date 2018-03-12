from collections import namedtuple
from textwrap import dedent


def clean(s):
    return dedent(s.lstrip('\n'))

class BottleCount(namedtuple('_bottlecount', 'value')):

    def __str__(self):
        if self.value == 0:
            return "No more bottles of beer"
        elif self.value == 1:
            return "1 bottle of beer"

        return f"{self.value} bottles of beer"

class BottleCounter:
    def __init__(self, start):
        self.current = start

    def __next__(self):
        if self.current == 0:
            return BottleCount(0), BottleCount(99)

        return BottleCount(self.current), BottleCount(self.current - 1)


class Verse:

    def matches(self, count: BottleCount):
        return count.value > 0

    def sing(self, current, _next):
        return (f"{current} on the wall\n"
                f"{current}\n"
                f"{self.action}\n"
                f"{_next} on the wall\n"
                )

    @property
    def action(self):
        return ("Take one down\n"
                "Pass it around")




class FinalVerse(Verse):

    def matches(self, count:BottleCount):
        return count.value == 0

    @property
    def action(self):
        return ("Go to the store\n"
                "Buy some more")




class BottleSong:

    _verses = [
        Verse(),
        FinalVerse()
    ]

    def verse(self, num):
        counter = BottleCounter(num)
        current, next_ = next(counter)
        for v in self._verses:
            if v.matches(current):
                return v.sing(current, next_)

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
