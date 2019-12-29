# Photomosaic
The purpose of this application is to build [photomosaic](https://en.wikipedia.org/wiki/Photographic_mosaic) images.

## Dependencies
Requires `Python 3` and `make` to be installed.

`make` will install local application dependencies:  
  * [Pillow](https://python-pillow.org/) for image mainpulation

## Usage
The `photomosaic.py` script is the application entry point.

Provide the source image and output file to generate a photomosaic:  
`./photomosaic.py -i test/data/christmas.jpeg -o test/data/out/mosaic.jpeg`

`./photomosaic.py -h`: outputs help text for full application argument details

## Samples
The samples below can be generated with `make sample` and will use the following source image:  
![source image](readme/source.jpg)

### Non-image Mosaic
The `none` image search (`-s`) option will use a direct color value for each tile in the mosaic. The resulting mosaic will resemble a blur effect of the source image.  
![non-image mosaic](readme/mosaic_no_image.jpg)

## Test Suite
`make test` will execute all tests from the `test/` directory
