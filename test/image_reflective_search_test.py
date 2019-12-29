from image_search import ImageSearchFactory

image_file = 'test/data/nature.jpg'

def test_search():
    xy = (2, 2)
    testSubject = ImageSearchFactory.ReflectiveSearch(xy, image_file)

    result = testSubject.search((10, 20, 30))

    assert len(result) == xy[0]
    for x in range(0, len(result)):
        assert len(result[x]) == xy[1]
        for y in range(0, len(result[x])):
            assert isinstance(result[x][y], tuple)
