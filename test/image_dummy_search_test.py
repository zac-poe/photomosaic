from image_search import ImageSearchFactory

def test_search():
    xy = (2, 2)
    testSubject = ImageSearchFactory.DummySearch(xy)

    pixel = (10, 20, 30)
    result = testSubject.search(pixel)

    assert len(result) == xy[0]
    for x in range(0, len(result)):
        assert len(result[x]) == xy[1]
        for y in range(0, len(result[x])):
            assert result[x][y] == pixel
