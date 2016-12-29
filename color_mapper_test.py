#!/usr/bin/python3

from color_mapper import ColorMapper

testSubject = ColorMapper()

def test_direct_red():
    assert testSubject.map([255,0,0]) == "red"

