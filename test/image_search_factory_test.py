from image_search import ImageSearchFactory

def test_construct_pixabay_search():
    searcher = ImageSearchFactory.construct('pixabay')

    assert isinstance(searcher, ImageSearchFactory.PixabaySearch)

def test_construct_unknown_type():
    try:
        ImageSearchFactory.construct('other')
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass
