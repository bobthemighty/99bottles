from textwrap import dedent

def clean(s):
    return dedent(s.lstrip('\n'))

class BottleSong:

    def describe_bottles(self, num):
        if num == 1:
            return "1 bottle"
        return f"{num} bottles"

    def verse(self, num):
        return clean(f"""
        {self.describe_bottles(num)} of beer on the wall
        {self.describe_bottles(num)} of beer
        Take one down
        Pass it around
        {self.describe_bottles(num - 1)} of beer on the wall
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


