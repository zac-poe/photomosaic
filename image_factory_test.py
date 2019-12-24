from image import ImageFactory
from PIL.Image import Image

testSubject = ImageFactory()

def test_create_image():
    x = 10
    y = 20
    image = testSubject.create(x, y)
    assert isinstance(image, Image)
    assert image.width == x
    assert image.height == y
