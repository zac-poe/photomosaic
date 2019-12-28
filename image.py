from PIL import Image, ImageFile

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
