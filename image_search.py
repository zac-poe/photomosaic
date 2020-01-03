from image_library import ImageLibrary

## creates image search instances
class ImageSearchFactory:
    SEARCH_PIXABAY = 'pixabay'

    @classmethod
    def construct(cls, source):
        if source == ImageSearchFactory.SEARCH_PIXABAY:
            return ImageSearchFactory.PixabaySearch()
        else:
            raise ValueError("unknown search source {0}".format(source))

    ## search implementation for Pixabay
    class PixabaySearch:
        def __init__(self):
            pass

        def search(self, color, quantity):
            pass
