import os
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
        API_KEY_FILE = '.pixabay_api_key'

        def __init__(self):
            key_file = open(os.path.dirname(os.path.realpath(__file__)) 
                + '/' + self.API_KEY_FILE, 'r')
            self.api_key = key_file.readline()

        def search(self, color, quantity):
            pass
