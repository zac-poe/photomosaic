from image_search import ImageSearchFactory

def test_construct_dummy_search():
    searcher = ImageSearchFactory.construct('none', (1,1))
    assert searcher != None

def test_construct_unsupported_type():
    try:
        ImageSearchFactory.construct('other', (1,1))
        raise RuntimeError("expected TypeError")
    except ValueError:
        pass
