from image_search import ImageSearchFactory
import os

def test_init_fails_on_missing_key():
    ImageSearchFactory.PixabaySearch.API_KEY_FILE = 'no_such_file'

    try:
        ImageSearchFactory.PixabaySearch()
        raise RuntimeException("expected file not found")
    except FileNotFoundError:
        pass

def test_init_reads_key():
    test_key = 'key.test'
    key_value = 'expected test key'
    ImageSearchFactory.PixabaySearch.API_KEY_FILE = test_key

    key_file = open(test_key, 'w')
    key_file.write(key_value)
    key_file.close()

    test_subject = ImageSearchFactory.PixabaySearch()

    assert key_value == test_subject.api_key

    os.remove(test_key)

# search tests are commented out since api keys will not be version controlled
'''
def test_search():
    ImageSearchFactory.PixabaySearch.API_KEY_FILE = '.pixabay_api_key'
    test_subject = ImageSearchFactory.PixabaySearch()
    quantity = 1

    results = test_subject.search('red', quantity)
    assert len(results) == quantity
'''
