from image import PixelAnalyzer

testSubject = PixelAnalyzer()

def test_average_same_value():
    pixel = (1, 2, 3)
    pixels = [
        [pixel, pixel],
        [pixel, pixel]
    ]

    assert pixel == testSubject.average(pixels)

def test_average():
    pixels = [
        [(10, 65, 111), (30, 85, 133)],
        [(20, 75, 122), (40, 95, 144)]
    ]

    assert (25, 80, 128) == testSubject.average(pixels)
