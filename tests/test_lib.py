# tests/test_lib.py
from chris_pack.lib import say_who_dat

def test_say_who_dat():
    assert say_who_dat() == "WHO DAT?"
