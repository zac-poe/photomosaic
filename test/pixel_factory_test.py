from image import PixelFactory

def test_construct_rgb():
    pixelTuple = (1, 2, 3)

    pixelObj = PixelFactory.parse(pixelTuple)

    assert pixelTuple == pixelObj.to_tuple()

def test_construct_unsupported_type():
    try:
        PixelFactory.parse((1,2))
        raise RuntimeError("expected TypeError")
    except TypeError:
        pass
