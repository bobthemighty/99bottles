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


class BottleSong:

    def describe_bottles(self, num):
        if num == 1:
            return "1 bottle"
        if num == 0:
            return "No more bottles"
        return f"{num} bottles"

    def verse(self, num):
        current = BottleCount(num)
        next = BottleCount(num - 1) if num > 0 else BottleCount(99)
        if num > 0:
            return clean(f"""
            {current} on the wall
            {current}
            Take one down
            Pass it around
            {next} on the wall
            """)
        else:
            return clean(f"""
            {current} on the wall
            {current}
            Go to the store
            Buy some more
            {next} on the wall
            """)


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
