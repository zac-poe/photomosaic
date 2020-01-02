from image_library import ImageRetrievalFactory, ImageLibrary
from unittest.mock import MagicMock

def test_load_library_initializes_library():
    image_library = MagicMock(spec=ImageLibrary)
    test_subject = ImageRetrievalFactory.LibraryRetrieval((0,0))

    test_subject.load_library(image_library)

    image_library.init.assert_called_with()

def test_load_library_fails_with_invalid_object():
    test_subject = ImageRetrievalFactory.LibraryRetrieval((0,0))

    try:
        test_subject.load_library('image_library')
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass

def test_get_pixel():
    xy = (2, 2)
    image_library = MagicMock(spec=ImageLibrary)
    test_subject = ImageRetrievalFactory.LibraryRetrieval(xy)

    test_subject.load_library(image_library)
    image_library.next.return_value = 'test/data/nature.jpg'

    result = test_subject.get((10, 20, 30))

    assert isinstance(result, list)
    assert isinstance(result[0], list)

def test_get_fails_when_library_has_not_been_loaded():
    xy = (2, 2)
    test_subject = ImageRetrievalFactory.LibraryRetrieval(xy)

    try:
        test_subject.get((10, 20, 30))
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass
