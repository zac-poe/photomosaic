from image import PixelFactory

def test_combine_adds_values():
    pixelATuple = (1, 2, 3)
    pixelA = PixelFactory.RgbPixel(pixelATuple)
    pixelB = PixelFactory.RgbPixel((5, 6, 7))

    pixelA.combine_with(pixelB)

    assert pixelA.red == pixelATuple[0] + pixelB.red
    assert pixelA.green == pixelATuple[1] + pixelB.green
    assert pixelA.blue == pixelATuple[2] + pixelB.blue

def test_divide_divides_all_values():
    pixel = PixelFactory.RgbPixel((2, 4, 6))

    pixel.divide(2)

    assert pixel.red == 1
    assert pixel.green == 2
    assert pixel.blue == 3

def test_divide_handles_bad_value():
    try:
        PixelFactory.RgbPixel((1,1,1)).divide('a')
        raise RuntimeError("expected value error")
    except ValueError:
        pass

def test_divide_rounds():
    pixel = PixelFactory.RgbPixel((3, 3, 3))

    pixel.divide(2)

    assert pixel.red == 2
    assert pixel.green == 2
    assert pixel.blue == 2

def test_divide_limits_to_max_value():
    pixel = PixelFactory.RgbPixel((300, 290, 400))

    pixel.divide(1)

    assert pixel.red == PixelFactory.RgbPixel.MAX_VALUE
    assert pixel.green == PixelFactory.RgbPixel.MAX_VALUE
    assert pixel.blue == PixelFactory.RgbPixel.MAX_VALUE

def test_distance_between_same_pixels_is_0():
    pixel = PixelFactory.RgbPixel((255, 0, 0))

    assert 0 == pixel.distance(pixel)

def test_max_distance_between_pixels_is_valid():
    pixel = PixelFactory.RgbPixel((255,255,255))

    assert PixelFactory.MAX_PIXEL_DISTANCE > \
        pixel.distance(PixelFactory.RgbPixel((0,0,0)))
