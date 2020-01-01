from image_library import ImageRetrievalFactory

def test_construct_dummy_search():
    retriever = ImageRetrievalFactory.construct('none', (1,1), 'n/a')
    assert retriever != None

def test_construct_self_search():
    retriever = ImageRetrievalFactory.construct('self', (1,1), 'test/data/nature.jpg')
    assert retriever != None

def test_construct_library_search():
    retriever = ImageRetrievalFactory.construct('library', (1,1), 'n/a')
    assert retriever != None

def test_construct_unsupported_type():
    try:
        ImageRetrievalFactory.construct('other', (1,1), 'n/a')
        raise RuntimeError("expected TypeError")
    except ValueError:
        pass
