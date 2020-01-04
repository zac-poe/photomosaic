import os
import requests
import math

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
        API_URL = 'https://pixabay.com/api/'
        API_KEY_FILE = '.pixabay_api_key'
        PAGE_SIZE = 20

        def __init__(self):
            key_file = open(os.path.dirname(os.path.realpath(__file__)) 
                + '/' + self.API_KEY_FILE, 'r')
            self.api_key = key_file.readline()

        def search(self, color, quantity):
            images = []
            for page in range(1, math.ceil(quantity / self.PAGE_SIZE) + 1):
                result = requests.get(self.API_URL,
                    params = {
                        'key': self.api_key,
                        'colors': color,
                        'page': page
                    }).json()

                for i in range(0, min(quantity - len(images), 20)):
                    images.append(result['hits'][i]['previewURL'])
            return images


## for handling search results
class SearchResultHandler:
    def __init__(self, directory):
        if not os.path.isdir(directory):
            raise ValueError("search result directory {0} does not exist"
                .format(directory))
        self.directory = directory

    def download(self, url):
        response = requests.get(url)
        filename = self.directory + '/' + os.path.basename(url)
        file = open(filename, 'wb')
        file.write(response.content)
        return filename
