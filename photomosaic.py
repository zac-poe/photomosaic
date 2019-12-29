#!/usr/bin/python3

import argparse
from image import ImageMapper, PixelAnalyzer
from mosaic import Mosaic
from image_search import ImageSearchFactory

# application option arguments
arg_parser = argparse.ArgumentParser(description='Generates photomosaic images.')
arg_parser.add_argument('-i',
    dest='input_file',
    type=str,
    required=True,
    help='Source input image')
arg_parser.add_argument('-s',
    dest='search_type',
    type=str,
    default=ImageSearchFactory.SEARCH_NONE,
    choices=[ImageSearchFactory.SEARCH_NONE],
    help='Mosaic tile search type (default: %(default)s)')
arg_parser.add_argument('-t',
    dest='thumb_size',
    type=int,
    default=20,
    help='Mosaic thumbnail tile square dimensions (default: %(default)s)')
arg_parser.add_argument('-x',
    dest='x',
    type=int,
    help='Mosaic thumbnail tile X dimension')
arg_parser.add_argument('-y',
    dest='y',
    type=int,
    help='Mosaic thumbnail tile Y dimension')
arg_parser.add_argument('-o',
    dest='output_file',
    type=str,
    required=True,
    help='Mosaic output image name')

args = arg_parser.parse_args()

# mosaic creation constructs
dimensions = (args.x or args.thumb_size,
    args.y or args.thumb_size)
image_mapper = ImageMapper()
mosaic_builder = Mosaic()
pixel_analyzer = PixelAnalyzer()
image_searcher = ImageSearchFactory.construct(args.search_type, dimensions)

print("Parsing source image...")
mosaic = mosaic_builder.tile(image_mapper.read_pixels(args.input_file), dimensions)

print("Generating photomosaic...")
for i in range(0, len(mosaic)):
    for j in range(0, len(mosaic[i])):
        mosaic[i][j] = image_searcher.search(pixel_analyzer.average(mosaic[i][j]))

image_mapper.write_pixels(mosaic_builder.untile(mosaic), args.output_file)
print("Photomosaic creation complete!")
