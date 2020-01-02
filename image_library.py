import collections
from image import ImageMapper, PixelFactory
from PIL import Image
import os

## creates image search instances
class ImageRetrievalFactory:
    RETRIEVE_LIBRARY = 'library'
    RETRIEVE_REFLECTIVE = 'self'
    RETRIEVE_NONE = 'none'

    @classmethod
    def construct(cls, type, xy, original):
        if not isinstance(type, str):
            raise ValueError("Requested type must be a string")
        if not isinstance(xy, collections.Sequence) or len(xy) < 2 \
            or not isinstance(xy[0], int) or xy[0] < 0 \
            or not isinstance(xy[1], int) or xy[1] < 0:
            raise ValueError("Providex xy must be sequence of two positive numbers")
        if type.lower() == ImageRetrievalFactory.RETRIEVE_NONE:
            return ImageRetrievalFactory.DummyRetrieval(xy)
        if type.lower() == ImageRetrievalFactory.RETRIEVE_REFLECTIVE:
            return ImageRetrievalFactory.ReflectiveRetrieval(xy, original)
        if type.lower() == ImageRetrievalFactory.RETRIEVE_LIBRARY:
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
            self.image_mapper = ImageMapper()
            self.xy = xy

        def load_library(self, library):
            if not isinstance(library, ImageLibrary):
                raise ValueError("library must be an ImageLibrary")
            self.image_library = library
            self.image_library.init()

        def get(self, pixel):
            if not hasattr(self, 'image_library'):
                raise ValueError("no image library has been loaded")

            # retrieve image
            file = self.image_library.next(pixel)
            image = self.image_mapper.read_file(file).resize(self.xy)

            # mask to specific color tone
            image = self.image_mapper.colorize_image(image, pixel)

            return self.image_mapper.read_image(image)


## provides behavior for interactions with local image file library
class ImageLibrary:
    LIBRARY_NAME = 'image_library'

    def __init__(self, library_name=LIBRARY_NAME):
        self.library_path = os.path.dirname(os.path.realpath(__file__)) \
            + '/' + library_name
        self.color_mapper = ImageLibrary.ColorMapper()

    def init(self):
        self.library_files = {}

        warning_msg = "Has this library been initialized with build_library.py?"
        try:
            library_dirs = os.listdir(self.library_path)
        except FileNotFoundError:
            raise self.ImageLibraryError("No image library found at {0}. {1}"
                .format(self.library_path, warning_msg))
        for color in self.ColorMapper.COLOR_SPECTRUM:
            if not color in library_dirs:
                raise self.ImageLibraryError(
                    "Local image library is missing color {0}. {1}"
                    .format(color, warning_msg))

            images = os.listdir(self.library_path + '/' + color)

            if not len(images) > 0:
                raise self.ImageLibraryError(
                    "Local image library has no images under folder {0}. {1}"
                    .format(color, warning_msg))

            self.library_files[color] = [0, images]

    def next(self, pixel):
        if not hasattr(self, 'library_files'):
            raise self.ImageLibraryError("This object has not been initialized")

        color = self.color_mapper.name(pixel)

        color_list = self.library_files[color]
        index = color_list[0]

        # we have reached the end of the image files for this color
        if index >= len(color_list[1]):
            index = 0

        # increment for next retrieval
        self.library_files[color][0] = index + 1

        return "{0}/{1}/{2}".format(
                self.library_path,
                color,
                self.library_files[color][1][index]
            )

    ## for reporting out library state issues
    class ImageLibraryError(Exception):
        def __init__(self, message):
            self.message = message

        def __str__(self):
            return repr(self.message)

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
