from image import ImageMapper
import collections

testSubject = ImageMapper()

def test_read_pixels():
    result = testSubject.read_pixels('test-data/nature.jpg')
    assert isinstance(result, collections.Sequence)  # image map
    assert isinstance(result[0], collections.Sequence)  # row map
    assert isinstance(result[0][0], collections.Sequence)  # pixel

def test_write_pixels():
    file = 'test-data/test-out.jpg'
    colors = [(255,0,0),(0,255,0),(0,0,255)]
    colorsX = 30
    y = 100
    pixels = []
    for i in range(0, y):
        row = []
        for c in colors:
            for j in range(0, colorsX):
                row.append(c)
        pixels += [row]
    testSubject.write_pixels(pixels, file)
    image = testSubject.read_pixels(file)
    assert len(image) == y  # height
    assert len(image[0]) == len(colors) * colorsX  # width

def test_write_pixels_uneven_descending():
    file = 'test-data/test-out-failure-1.jpg'
    pixels = [
        [(0,0,0),(0,0,0),(0,0,0)],
        [(0,0,0),(0,0,0)],
        [(0,0,0)]
    ]
    try:
        testSubject.write_pixels(pixels, file)
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass

def test_write_pixels_uneven_ascending():
    file = 'test-data/test-out-failure-2.jpg'
    pixels = [
        [(0,0,0)],
        [(0,0,0),(0,0,0)],
        [(0,0,0),(0,0,0),(0,0,0)]
    ]
    try:
        testSubject.write_pixels(pixels, file)
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass
