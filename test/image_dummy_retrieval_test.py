from image_library import ImageRetrievalFactory

def test_get_pixel():
    xy = (2, 2)
    testSubject = ImageRetrievalFactory.DummyRetrieval(xy)

    pixel = (10, 20, 30)
    result = testSubject.get(pixel)

    assert len(result) == xy[0]
    for x in range(0, len(result)):
        assert len(result[x]) == xy[1]
        for y in range(0, len(result[x])):
            assert result[x][y] == pixel
