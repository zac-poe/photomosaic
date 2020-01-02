import collections
from image import ImageMapper, PixelFactory
from PIL import Image

## creates image search instances
class ImageRetrievalFactory:
    SEARCH_LIBRARY = 'library'
    SEARCH_REFLECTIVE = 'self'
    SEARCH_NONE = 'none'

    @classmethod
    def construct(cls, type, xy, original):
        if not isinstance(type, str):
            raise ValueError("Requested type must be a string")
        if not isinstance(xy, collections.Sequence) or len(xy) < 2 \
            or not isinstance(xy[0], int) or xy[0] < 0 \
            or not isinstance(xy[1], int) or xy[1] < 0:
            raise ValueError("Providex xy must be sequence of two positive numbers")
        if type.lower() == ImageRetrievalFactory.SEARCH_NONE:
            return ImageRetrievalFactory.DummyRetrieval(xy)
        if type.lower() == ImageRetrievalFactory.SEARCH_REFLECTIVE:
            return ImageRetrievalFactory.ReflectiveRetrieval(xy, original)
        if type.lower() == ImageRetrievalFactory.SEARCH_LIBRARY:
            return ImageRetrievalFactory.LibraryRetrieval(xy)
        else:
            raise ValueError("Type {0} is not supported".format(type))

    ## non-image file retrieval, provides result matching search color
    class DummyRetrieval:
        def __init__(self, xy):
            self.x = xy[0]
            self.y = xy[1]

        def get(self, pixel):
            result = []
            for x in range(0, self.x):
                column = []
                for y in range(0, self.y):
                    column += [pixel]
                result += [column]
            return result

    ## uses seed image, hue-ed to matching search color
    class ReflectiveRetrieval:
        def __init__(self, xy, image):
            self.image_mapper = ImageMapper()
            self.image = self.image_mapper.read_file(image).resize(xy)

        def get(self, pixel):
            return self.image_mapper.read_image(
                self.image_mapper.colorize_image(self.image, pixel)
            )

    ## uses a local library to retrieve and mask results
    class LibraryRetrieval:
        def __init__(self, xy):
            self.x = xy[0]
            self.y = xy[1]

        def get(self, pixel):
            result = []
            return result


class ImageLibrary:
    ## maps from pixels to library colors
    class ColorMapper:
        COLOR_SPECTRUM = {
            'black': PixelFactory.parse((0, 0, 0)),
            'blue': PixelFactory.parse((0, 0, 255)),
            'brown': PixelFactory.parse((150, 75, 0)),
            'gray': PixelFactory.parse((128, 128, 128)),
            'green': PixelFactory.parse((0, 255, 0)),
            'lilac': PixelFactory.parse((200, 162, 200)),
            'orange': PixelFactory.parse((255, 79, 0)),
            'pink': PixelFactory.parse((255, 166, 201)),
            'red': PixelFactory.parse((255, 0, 0)),
            'turquoise': PixelFactory.parse((64, 224, 208)),
            'white': PixelFactory.parse((255, 255, 255)),
            'yellow': PixelFactory.parse((255, 255, 0))
        }

        def name(self, pixel):
            closest_distance = PixelFactory.MAX_PIXEL_DISTANCE
            result = 'white'
            pixel_object = PixelFactory.parse(pixel)

            for name, color in self.COLOR_SPECTRUM.items():
                color_distance = pixel_object.distance(color)
                if color_distance < closest_distance:
                    closest_distance = color_distance
                    result = name

            return result
