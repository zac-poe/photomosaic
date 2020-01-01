from image_library import ImageRetrievalFactory

image_file = 'test/data/nature.jpg'

def test_get_pixel():
    xy = (2, 2)
    testSubject = ImageRetrievalFactory.ReflectiveRetrieval(xy, image_file)

    result = testSubject.get((10, 20, 30))

    assert len(result) == xy[0]
    for x in range(0, len(result)):
        assert len(result[x]) == xy[1]
        for y in range(0, len(result[x])):
            assert isinstance(result[x][y], tuple)
