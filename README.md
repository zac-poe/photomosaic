# Photomosaic

The purpose of this application is to build [photomosaic](https://en.wikipedia.org/wiki/Photographic_mosaic) images.

## Dependencies
Requires `Python 3` and `make` to be installed.

`make` will install local application dependencies:  
  * [Pillow](https://python-pillow.org/) for image mainpulation

## Usage

## Samples
The samples below have been generated using the following source image:  
![source image](readme/source.jpg)

### Non-image Mosaic
The `none` image search option will use a direct color value for each tile in the mosaic. The resulting mosaic will resemble a blur effect of the source image.  
![non-image mosaic](readme/mosaic_no_image.jpg)

## Test Suite
`make test` will execute all tests from the `test/` directory
