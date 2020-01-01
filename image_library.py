import collections
from image import ImageMapper
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
