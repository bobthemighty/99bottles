from textwrap import dedent

def clean(s):
    return dedent(s.lstrip('\n'))

class BottleSong:

    def describe_bottles(self, num):
        if num == 1:
            return "1 bottle"
        if num == 0:
            return "No more bottles"
        return f"{num} bottles"

    def verse(self, num):
        if num > 0:
            return clean(f"""
            {self.describe_bottles(num)} of beer on the wall
            {self.describe_bottles(num)} of beer
            Take one down
            Pass it around
            {self.describe_bottles(num - 1)} of beer on the wall
            """)
        else:
            return clean(f"""
            {self.describe_bottles(num)} of beer on the wall
            {self.describe_bottles(num)} of beer
            Go to the store
            Buy some more
            99 bottles of beer on the wall
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
