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
    def __init__(self, start, end=0):
        self.current = start
        self.end = end
        self.done = False

    def __next__(self):
        if self.done:
            raise StopIteration()
        if self.current == self.end:
            self.done = True
        current = self.current
        _next = 99 if current == 0 else current - 1
        self.current = _next
        return BottleCount(current), BottleCount(_next)

    def __iter__(self):
        return self


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

    def sing(self, current, next_):
        for v in self._verses:
            if v.matches(current):
                return v.sing(current, next_)


    def verse(self, num):
        return self.verses(num, num)

    def verses(self, start, end=0):
        counter = BottleCounter(start, end)
        return "\n".join(
            self.sing(current, next_)
            for current, next_ in counter)


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
