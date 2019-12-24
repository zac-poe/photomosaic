from image import ImageFileReader
from PIL.Image import Image

testSubject = ImageFileReader()

def test_read_image():
    assert isinstance(testSubject.read('test-data/nature.jpg'), Image)
