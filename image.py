from PIL import Image, ImageFile

IMAGE_MODE = 'RGB'

## Supports mapping and unmapping between a file and basic data structures
class ImageMapper:
    # map an image file to a nested list of pixels
    def read_pixels(self, filename):
        pixels = []

        def read_file(filename):
            file = open(filename, 'rb')
            parser = ImageFile.Parser()
            parser.feed(file.read())
            return parser.close().convert(IMAGE_MODE)

        image = read_file(filename)
        for y in range(0, image.height):
            row = []
            for x in range(0, image.width):
                row += [image.getpixel((x, y))]
            pixels += [row]
        return pixels

    # write a nested list of pixels to image file
    def write_pixels(self, pixels, filename):
        y = len(pixels)
        x = len(pixels[0])
        image = Image.new(IMAGE_MODE, (x, y))

        for y in range(0, y):
            for x in range(0, x):
                image.putpixel((x, y),
                    pixels[y][x])

        image.save(filename)
