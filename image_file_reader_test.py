from image import ImageParser
from PIL.Image import Image

testSubject = ImageParser()

def test_read_image():
    assert isinstance(testSubject.read('test-data/nature.jpg'), Image)
