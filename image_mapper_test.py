from image import ImageMapper
import collections

testSubject = ImageMapper()

def test_read_pixels():
    result = testSubject.read_pixels('test-data/nature.jpg')
    assert isinstance(result, collections.Sequence)  # image map
    assert isinstance(result[0], collections.Sequence)  # row map
    assert isinstance(result[0][0], collections.Sequence)  # pixel

def test_read_pixels():
    file = 'test-data/test-out.jpg'
    testSubject.write_pixels([
            [(255,255,255),(255,0,0),(0,255,0),(0,0,255),(0,0,0)],
            [(255,255,255),(255,0,0),(0,255,0),(0,0,255),(0,0,0)],
            [(255,255,255),(255,0,0),(0,255,0),(0,0,255),(0,0,0)],
            [(255,255,255),(255,0,0),(0,255,0),(0,0,255),(0,0,0)],
            [(255,255,255),(255,0,0),(0,255,0),(0,0,255),(0,0,0)],
            [(255,255,255),(255,0,0),(0,255,0),(0,0,255),(0,0,0)],
            [(255,255,255),(255,0,0),(0,255,0),(0,0,255),(0,0,0)],
            [(255,255,255),(255,0,0),(0,255,0),(0,0,255),(0,0,0)]
        ], file)
    image = testSubject.read_pixels(file)
    assert len(image) == 8  # height
    assert len(image[0]) == 5  # width
