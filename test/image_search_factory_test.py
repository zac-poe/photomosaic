from image_search import ImageSearchFactory

def test_construct_dummy_search():
    searcher = ImageSearchFactory.construct('none', (1,1), 'n/a')
    assert searcher != None

def test_construct_self_search():
    searcher = ImageSearchFactory.construct('self', (1,1), 'test/data/nature.jpg')
    assert searcher != None

def test_construct_unsupported_type():
    try:
        ImageSearchFactory.construct('other', (1,1), 'n/a')
        raise RuntimeError("expected TypeError")
    except ValueError:
        pass
