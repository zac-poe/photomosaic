import collections
from image import ImageMapper
from PIL import Image

## creates image search instances
class ImageSearchFactory:
    SEARCH_NONE = 'none'
    SEARCH_REFLECTIVE = 'self'

    @classmethod
    def construct(cls, type, xy, original):
        if not isinstance(type, str):
            raise ValueError("Requested type must be a string")
        if not isinstance(xy, collections.Sequence) or len(xy) < 2 \
            or not isinstance(xy[0], int) or xy[0] < 0 \
            or not isinstance(xy[1], int) or xy[1] < 0:
            raise ValueError("Providex xy must be sequence of two positive numbers")
        if type.lower() == ImageSearchFactory.SEARCH_NONE:
            return ImageSearchFactory.DummySearch(xy)
        if type.lower() == ImageSearchFactory.SEARCH_REFLECTIVE:
            return ImageSearchFactory.ReflectiveSearch(xy, original)
        else:
            raise ValueError("Type {0} is not supported".format(type))

    ## non-searching, provides result matching search color
    class DummySearch:
        def __init__(self, xy):
            self.x = xy[0]
            self.y = xy[1]

        def search(self, pixel):
            result = []
            for x in range(0, self.x):
                column = []
                for y in range(0, self.y):
                    column += [pixel]
                result += [column]
            return result

    ## uses seed image, hue-ed to matching search color
    class ReflectiveSearch:
        def __init__(self, xy, image):
            self.image_mapper = ImageMapper()
            self.image = self.image_mapper.read_file(image).resize(xy)

        def search(self, pixel):
            base_image = self.image.copy().convert(ImageMapper.COMPOSITE_MODE)

            def colorize(image, pixel):
                for x in range(0, image.width):
                    for y in range(0, image.height):
                        image.putpixel((x, y), pixel)

            color_image = base_image.copy()
            colorize(color_image, pixel)

            return self.image_mapper.read_image(
                Image.blend(base_image, color_image, .75)
            )
