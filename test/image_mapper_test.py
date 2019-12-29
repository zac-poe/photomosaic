from image import ImageMapper
from PIL import Image
import collections

testSubject = ImageMapper()

def test_read_file():
    result = testSubject.read_file('test/data/nature.jpg')
    assert isinstance(result, Image.Image)

def test_read_pixels():
    result = testSubject.read_pixels('test/data/nature.jpg')
    assert isinstance(result, collections.Sequence)  # image map
    assert isinstance(result[0], collections.Sequence)  # col map
    assert isinstance(result[0][0], collections.Sequence)  # pixel

def test_read_image_equates_to_read_pixels():
    result = testSubject.read_image(testSubject.read_file('test/data/nature.jpg'))
    assert isinstance(result, collections.Sequence)  # image map
    assert isinstance(result[0], collections.Sequence)  # col map
    assert isinstance(result[0][0], collections.Sequence)  # pixel

def test_write_pixels():
    file = 'test/data/out/image-mapper.jpg'
    colors = [(255,0,0),(0,255,0),(0,0,255)]
    colorsX = 30
    y = 100
    pixels = []
    for c in colors:
        for i in range(0, colorsX):
            col = []
            for j in range(0, y):
                col.append(c)
            pixels += [col]
    testSubject.write_pixels(pixels, file)
    image = testSubject.read_pixels(file)
    assert len(image) == len(colors) * colorsX  # width
    assert len(image[0]) == y  # height

def test_write_pixels_uneven_descending():
    file = 'test/data/out/image-mapper-failure-1.jpg'
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
    file = 'test/data/out/image-mapper-failure-2.jpg'
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

def test_write_pixels_bad_pixels_argument():
    file = 'test/data/out/image-mapper-failure-3.jpg'
    try:
        testSubject.write_pixels("pixels", file)
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass

def test_write_pixels_non_nested_pixels():
    file = 'test/data/out/image-mapper-failure-4.jpg'
    pixels = [(0,0,0),(0,0,0),(0,0,0)]
    try:
        testSubject.write_pixels(pixels, file)
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass
