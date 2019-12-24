from image import ImageFileReader, ImageMapper
import collections

fileReader = ImageFileReader()
testSubject = ImageMapper()

def test_read_pixels():
    result = testSubject.read_pixels(fileReader.read('test-data/nature.jpg'))
    assert isinstance(result, collections.Sequence)  # image map
    assert isinstance(result[0], collections.Sequence)  # row map
    assert isinstance(result[0][0], collections.Sequence)  # pixel
