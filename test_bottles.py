from textwrap import dedent

def clean(s):
    return dedent(s.lstrip('\n'))

class BottleSong:

    def verse(self, num):
        return clean(f"""
        {num} bottles of beer on the wall
        {num} bottles of beer
        Take one down
        Pass it around
        {num - 1} bottles of beer on the wall
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
