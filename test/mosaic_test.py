from mosaic import Mosaic

testSubject = Mosaic()

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# In           Out
# RRGGBB  ==>  RR GG BB
# RRGGBB       RR GG BB
def test_tile_6_by_2_as_2_by_2():
    pixels = [
        [RED, RED],
        [RED, RED],
        [GREEN, GREEN],
        [GREEN, GREEN],
        [BLUE, BLUE],
        [BLUE, BLUE]
    ]
    mosaic = testSubject.tile(pixels, (2,2))
    assert len(mosaic) == 3
    assert len(mosaic[0]) == 1
    assert len(mosaic[1]) == 1
    assert len(mosaic[2]) == 1
    for x in range(0, 3):
        for y in range (0, 1):
            assert len(mosaic[x][y]) == 2
            for i in range(0, 2):
                assert len(mosaic[x][y][i]) == 2
                for j in range(0, 2):
                    if x == 0:
                        color = RED
                    elif x == 1:
                        color = GREEN
                    else:
                        color = BLUE
                    assert mosaic[x][y][i][j] == color

# In       Out
# BB       BB
# BB  ==>  BB
# GG
# GG       GG
# RR       GG
# RR
#          RR
#          RR
def test_tile_2_by_6_as_2_by_2():
    pixels = [
        [RED, RED, GREEN, GREEN, BLUE, BLUE],
        [RED, RED, GREEN, GREEN, BLUE, BLUE]
    ]
    mosaic = testSubject.tile(pixels, (2,2))
    assert len(mosaic) == 1
    assert len(mosaic[0]) == 3
    for x in range(0, 1):
        for y in range (0, 3):
            assert len(mosaic[x][y]) == 2
            for i in range(0, 2):
                assert len(mosaic[x][y][i]) == 2
                for j in range(0, 2):
                    if y == 0:
                        color = RED
                    elif y == 1:
                        color = GREEN
                    else:
                        color = BLUE
                    assert mosaic[x][y][i][j] == color

# In       Out
# BBB      BB B
# GGG  ==>
# RRR      GG G
#          RR R
def test_tile_with_remainder_3_by_3_as_2_by_2():
    pixels = [
        [RED, GREEN, BLUE],
        [RED, GREEN, BLUE],
        [RED, GREEN, BLUE]
    ]
    mosaic = testSubject.tile(pixels, (2,2))
    assert len(mosaic) == 2
    assert len(mosaic[0]) == 2
    assert len(mosaic[1]) == 2
    for x in range(0, 2):
        for y in range (0, 2):
            if x == 0:
                assert len(mosaic[x][y]) == 2
            else:
                assert len(mosaic[x][y]) == 1
            for i in range(0, len(mosaic[x][y])):
                if y == 0:
                    assert len(mosaic[x][y][i]) == 2
                else:
                    assert len(mosaic[x][y][i]) == 1
                for j in range(0, len(mosaic[x][y][i])):
                    if y == 0 and j == 0:
                        color = RED
                    elif y== 0 and j == 1:
                        color = GREEN
                    else:
                        color = BLUE
                    assert mosaic[x][y][i][j] == color

def test_tile_uneven_descending():
    pixels = [
        [RED,RED,RED],
        [RED,RED],
        [RED]
    ]
    try:
        testSubject.tile(pixels, (1,1))
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass

def test_tile_uneven_ascending():
    pixels = [
        [RED],
        [RED,RED],
        [RED,RED,RED]
    ]
    try:
        testSubject.tile(pixels, (1,1))
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass

def test_tile_bad_pixels_argument():
    try:
        testSubject.tile("pixels", (1,1))
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass

def test_tile_non_nested_pixels():
    pixels = [RED,RED]
    try:
        testSubject.tile(pixels, (1,1))
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass

def test_tile_bad_tile_dimensions_argument():
    dimensions = "dimensions"
    try:
        testSubject.tile([
                [RED,RED],
                [RED,RED]
            ], dimensions)
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass

def test_tile_no_tile_dimensions():
    dimensions = ()
    try:
        testSubject.tile([
                [RED,RED],
                [RED,RED]
            ], dimensions)
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass

def test_tile_missing_y_tile_dimension():
    dimensions = (5)
    try:
        testSubject.tile([
                [RED,RED],
                [RED,RED]
            ], dimensions)
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass

def test_tile_non_numeric_x_tile_dimension():
    dimensions = ("a",5)
    try:
        testSubject.tile([
                [RED,RED],
                [RED,RED]
            ], dimensions)
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass

def test_tile_non_numeric_y_tile_dimension():
    dimensions = (5,"a")
    try:
        testSubject.tile([
                [RED,RED],
                [RED,RED]
            ], dimensions)
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass

# In           Out
# RR GG BB ==> RRGGBB
# RR GG BB     RRGGBB
def test_untile_to_6_by_2():
    tiles = [
        [
            [
                [RED, RED],
                [RED, RED]
            ]
        ],
        [
            [
                [GREEN, GREEN],
                [GREEN, GREEN]
            ]
        ],
        [
            [
                [BLUE, BLUE],
                [BLUE, BLUE]
            ]
        ]
    ]
    pixels = testSubject.untile(tiles)
    assert len(pixels) == 6
    for x in range(0, len(pixels)):
        assert len(pixels[x]) == 2
        for y in range (0, len(pixels[x])):
            if x < 2:
                color = RED
            elif x < 4:
                color = GREEN
            else:
                color = BLUE
            assert pixels[x][y] == color

# In       Out
# BB       BB
# BB       BB
#          GG
# GG  ==>  GG
# GG       RR
#          RR
# RR
# RR
def test_untile_to_2_by_6():
    tiles = [
        [
            [
                [RED, RED],
                [RED, RED]
            ],
            [
                [GREEN, GREEN],
                [GREEN, GREEN]
            ],
            [
                [BLUE, BLUE],
                [BLUE, BLUE]
            ]
        ]
    ]
    pixels = testSubject.untile(tiles)
    assert len(pixels) == 2
    for x in range(0, len(pixels)):
        assert len(pixels[x]) == 6
        for y in range (0, len(pixels[x])):
            if y < 2:
                color = RED
            elif y < 4:
                color = GREEN
            else:
                color = BLUE
            assert pixels[x][y] == color

# In       Out
# BB B      BBB
#      ==>  GGG
# GG G      RRR
# RR R
def test_untile_uneven_to_3_by_3():
    tiles = [
        [
            [
                [RED, GREEN],
                [RED, GREEN]
            ],
            [
                [BLUE],
                [BLUE]
            ]
        ],
        [
            [
                [RED, GREEN]
            ],
            [
                [BLUE]
            ]
        ]
    ]
    pixels = testSubject.untile(tiles)
    assert len(pixels) == 3
    for x in range(0, len(pixels)):
        assert len(pixels[x]) == 3
        for y in range (0, len(pixels[x])):
            if y == 0:
                color = RED
            elif y == 1:
                color = GREEN
            else:
                color = BLUE
            assert pixels[x][y] == color

def test_untile_bad_tiles_argument():
    try:
        testSubject.untile("tiles")
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass

def test_untile_non_nested_tiles():
    tiles = [RED,RED]
    try:
        testSubject.untile(tiles)
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass

def test_untile_uneven_descending():
    tiles = [
        [
            [
                [RED]
            ],
            [
                [RED]
            ],
            [
                [RED]
            ]
        ],
        [
            [
                [RED]
            ],
            [
                [RED]
            ]
        ],
        [
            [
                [RED]
            ]
        ]
    ]
    try:
        testSubject.untile(tiles)
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass

def test_untile_uneven_ascending():
    tiles = [
        [
            [
                [RED]
            ]
        ],
        [
            [
                [RED]
            ],
            [
                [RED]
            ]
        ],
        [
            [
                [RED]
            ],
            [
                [RED]
            ],
            [
                [RED]
            ]
        ]
    ]
    try:
        testSubject.untile(tiles)
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass

def test_untile_bad_tile():
    tiles = [
        [
            "tile"
        ]
    ]
    try:
        testSubject.untile(tiles)
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass

def test_untile_non_nested_tile():
    tiles = [
        [
            [
                "tile"
            ]
        ]
    ]
    try:
        testSubject.untile(tiles)
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass

def test_untile_uneven_tile_pixel_columns():
    tiles = [
        [
            [
                [RED, RED],
                [RED]
            ]
        ],
        [
            [
                [RED, RED],
                [RED, RED]
            ]
        ]
    ]
    try:
        testSubject.untile(tiles)
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass
