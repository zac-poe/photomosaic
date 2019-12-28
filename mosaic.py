import collections

## Supports mapping between a nested list pixel data structure
## and a tile based mosaic
class Mosaic:
    # divides a nested list of pixels into a nested list of mosaic tiles
    # containing the respective x-by-y lists of pixels
    def tile(self, pixels, xy=(10,10)):
        if not isinstance(pixels, list) or not isinstance(pixels[0], list):
            raise ValueError("Provided pixels must be a nested list")
        if not isinstance(xy, collections.Sequence) or len(xy) < 2 \
            or not isinstance(xy[0], int) or xy[0] < 0 \
            or not isinstance(xy[1], int) or xy[1] < 0:
            raise ValueError("Providex xy must be sequence of two positive numbers")

        tiles = []
        maxY = len(pixels[0])

        tileX = 0
        for x in range(0, len(pixels)):
            if tileX >= len(tiles):
                tiles.append([])
            xWithinTile = x % xy[0]
            tileY = 0
            for y in range(0, maxY):
                if maxY != len(pixels[x]):
                    raise ValueError("Uneven pixels list provided")
                if tileY >= len(tiles[tileX]):
                    tiles[tileX].append([])
                if xWithinTile >= len(tiles[tileX][tileY]):
                    tiles[tileX][tileY].append([])
                tiles[tileX][tileY][xWithinTile].append(pixels[x][y])
                if (y+1) % xy[1] == 0:
                    tileY += 1
            if (x+1) % xy[0] == 0:
                tileX += 1
        return tiles
