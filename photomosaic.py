#!/usr/bin/python3

from image import ImageMapper, PixelAnalyzer
from mosaic import Mosaic
from image_search import ImageSearchFactory

mosaic_file = 'test/data/out/mosaic_no_image.jpeg'
source_file = 'test/data/christmas.jpeg'
thumb_size = 25
search_type = 'none'

# mosaic creation constructs
dimensions = (thumb_size, thumb_size)
image_mapper = ImageMapper()
mosaic_builder = Mosaic()
pixel_analyzer = PixelAnalyzer()
image_searcher = ImageSearchFactory.construct(search_type, dimensions)

print("Parsing source image...")
mosaic = mosaic_builder.tile(image_mapper.read_pixels(source_file), dimensions)

print("Generating photomosaic...")
for i in range(0, len(mosaic)):
    for j in range(0, len(mosaic[i])):
        mosaic[i][j] = image_searcher.search(pixel_analyzer.average(mosaic[i][j]))

image_mapper.write_pixels(mosaic_builder.untile(mosaic), mosaic_file)
print("Photomosaic creation complete!")
