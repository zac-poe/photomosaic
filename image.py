from PIL import Image, ImageFile
import collections

#
# docs: https://pillow.readthedocs.io/en/stable/reference/index.html
#

IMAGE_MODE = 'RGB'

## Supports mapping and unmapping between a file and basic data structures
class ImageMapper:
    # map an image file to a nested list of pixel tuples
    def read_pixels(self, filename):
        pixels = []

        def read_file(filename):
            file = open(filename, 'rb')
            parser = ImageFile.Parser()
            parser.feed(file.read())
            return parser.close().convert(IMAGE_MODE)

        image = read_file(filename)
        for x in range(0, image.width):
            column = []
            for y in range(0, image.height):
                column += [image.getpixel((x, y))]
            pixels += [column]
        return pixels

    # write a nested list of pixel tuples to image file
    def write_pixels(self, pixels, filename):
        if not isinstance(pixels, list) or not isinstance(pixels[0], list):
            raise ValueError("Provided pixels must be a nested list")

        maxX = len(pixels)
        maxY = len(pixels[0])
        image = Image.new(IMAGE_MODE, (maxX, maxY))

        for x in range(0, maxX):
            for y in range(0, maxY):
                if maxY != len(pixels[x]):
                    raise ValueError("Uneven pixels list provided")
                image.putpixel((x, y), pixels[x][y])

        image.save(filename)

## Supports analysis of nested pixel lists
class PixelAnalyzer:
    # produces average color from pixel map
    def average(self, pixels):
        if not isinstance(pixels, list) or not isinstance(pixels[0], list):
            raise ValueError("Provided pixels must be a nested list")

        maxX = len(pixels)
        maxY = len(pixels[0])
        pixel = PixelFactory.parse(pixels[0][0])

        for x in range(0, maxX):
            for y in range(0, maxY):
                if x == 0 and y == 0:
                    continue
                if maxY != len(pixels[x]):
                    raise ValueError("Uneven pixels list provided")
                pixel.combine(PixelFactory.parse(pixels[x][y]))
        pixel.divide(maxX * maxY)

        return pixel.to_tuple()

## Interprets and constructs pixel objects
class PixelFactory:
    @classmethod
    def parse(cls, pixel):
        if isinstance(pixel, collections.Sequence):
            if len(pixel) == 3:
                return PixelFactory.RgbPixel(pixel)
        raise TypeError("Unknown pixel format: {0}".format(pixel))

    ## implementation of PixelFactory contract: red, gren, blue pixel type
    class RgbPixel:
        MAX_VALUE = 255

        def __init__(self, tuple):
            self.red = tuple[0]
            self.green = tuple[1]
            self.blue = tuple[2]

        def combine(self, pixel):
            self.red += pixel.red
            self.green += pixel.green
            self.blue += pixel.blue

        def divide(self, quantity):
            if not isinstance(quantity, int) or quantity < 0:
                raise ValueError("{0} must be a positive integer"
                    .format(quantity))
            average = lambda v, q: min(round(v / q), PixelFactory.RgbPixel.MAX_VALUE)
            self.red = average(self.red, quantity)
            self.green = average(self.green, quantity)
            self.blue = average(self.blue, quantity)

        def to_tuple(self):
            return (self.red, self.green, self.blue)
