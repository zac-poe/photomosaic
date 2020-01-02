from PIL import Image, ImageFile
import collections
import math

## Supports mapping and unmapping between a file and basic data structures
class ImageMapper:
    IMAGE_MODE = 'RGB'
    COMPOSITE_MODE = 'RGBA'

    # map an image file to an Image object
    def read_file(self, filename):
        file = open(filename, 'rb')
        parser = ImageFile.Parser()
        parser.feed(file.read())
        return parser.close().convert(ImageMapper.IMAGE_MODE)

    # map an Image object to a nested list of pixel tuples
    def read_image(self, image):
        if not isinstance(image, Image.Image):
            raise ValueError("image must be instance of Image object")
        image = image.convert(ImageMapper.IMAGE_MODE)
        pixels = []
        for x in range(0, image.width):
            column = []
            for y in range(0, image.height):
                column += [image.getpixel((x, y))]
            pixels += [column]
        return pixels

    # shorthand to map an image file to a nested list of pixel tuples
    def read_pixels(self, filename):
        return self.read_image(self.read_file(filename))

    # write a nested list of pixel tuples to image file
    def write_pixels(self, pixels, filename):
        if not isinstance(pixels, list) or not isinstance(pixels[0], list):
            raise ValueError("Provided pixels must be a nested list")

        maxX = len(pixels)
        maxY = len(pixels[0])
        image = Image.new(ImageMapper.IMAGE_MODE, (maxX, maxY))

        for x in range(0, maxX):
            for y in range(0, maxY):
                if maxY != len(pixels[x]):
                    raise ValueError("Uneven pixels list provided")
                image.putpixel((x, y), pixels[x][y])

        image.save(filename)

    # applies a color mask of the given pixel to the given image
    def colorize_image(self, image, pixel):
        base_image = image.copy().convert(ImageMapper.COMPOSITE_MODE)
        color_image = base_image.copy()

        for x in range(0, color_image.width):
            for y in range(0, color_image.height):
                color_image.putpixel((x, y), pixel)

        return Image.blend(base_image, color_image, .75)


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
                pixel.combine_with(PixelFactory.parse(pixels[x][y]))
        pixel.divide(maxX * maxY)

        return pixel.to_tuple()


## Interprets and constructs pixel objects
class PixelFactory:
    MAX_PIXEL_DISTANCE = 450

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

        def combine_with(self, pixel):
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

        def distance(self, pixel):
            def square(n):
                return math.pow(n, 2)

            # returns 3d coordinate difference between pixels
            return math.sqrt(square(self.red - pixel.red)
                + square(self.green - pixel.green)
                + square(self.blue - pixel.blue))

        def to_tuple(self):
            return (self.red, self.green, self.blue)
