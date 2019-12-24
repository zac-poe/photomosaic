from PIL import Image, ImageFile

IMAGE_MODE = 'RGB'

class ImageFileReader:
    # read a given image file to an Image object
    def read(self, filename):
        file = open(filename, 'rb')
        parser = ImageFile.Parser()
        parser.feed(file.read())
        return parser.close().convert(IMAGE_MODE)

class ImageMapper:
    # map an image file to a nested list of pixels
    def read_pixels(self, image):
        pixels = []
        for y in range(0, image.height):
            row = []
            for x in range(0, image.width):
                row += [image.getpixel((x, y))]
            pixels += [row]
        return pixels

class ImageFactory:
    # creates a new image object for the given dimensions
    def create(self, x, y):
        return Image.new(IMAGE_MODE, (x, y))
