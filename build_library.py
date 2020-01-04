#!/usr/bin/python3

import argparse
from image_library import ImageLibrary
from image_search import ImageSearchFactory, SearchResultHandler
from image import ImageMapper
import os

# application option arguments
arg_parser = argparse.ArgumentParser(description='Builds an image library from Internet searches.')
arg_parser.add_argument('-s',
    dest='search_source',
    type=str,
    default=ImageSearchFactory.SEARCH_PIXABAY,
    choices=[ ImageSearchFactory.SEARCH_PIXABAY ],
    help='Search source (default: %(default)s)')
arg_parser.add_argument('-n',
    dest='num_results',
    type=int,
    default=500,
    help='Number of search results per color (default: %(default)s)')
arg_parser.add_argument('-t',
    dest='thumbnail_size',
    type=int,
    default=50,
    help='Target thumbnail size to scale to (default: %(default)s)')

args = arg_parser.parse_args()

image_library = ImageLibrary()
searcher = ImageSearchFactory.construct(args.search_source)
image_mapper = ImageMapper()

print("Creating empty image library...")
image_library.create()
result_handler = SearchResultHandler(image_library.LIBRARY_NAME)

print("Building library...")
for color in ImageLibrary.COLORS:
    print("\tSearching for {0} images...".format(color))
    for url in searcher.search(color, args.num_results):
        file = result_handler.download(url)
        image_library.add_file(color, file, args.thumbnail_size)

print("Image library build complete!")
