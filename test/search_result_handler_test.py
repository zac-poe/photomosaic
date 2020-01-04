from image_search import SearchResultHandler
import os
import shutil

download_directory = 'test_download'

def test_download_retrieves_file():
    setup()
    test_subject = SearchResultHandler(download_directory)
    file = 'logo_square.png'

    test_subject.download("https://pixabay.com/static/img/" + file)

    assert os.path.exists(download_directory + '/' + file)

    tear_down()

def test_init_fails_when_directory_is_missing():
    tear_down()

    try:
        SearchResultHandler(download_directory)
        raise RuntimeError("expected ValueError")
    except ValueError:
        pass

def setup():
    tear_down()
    os.mkdir(download_directory)

def tear_down():
    if os.path.isdir(download_directory):
        shutil.rmtree(download_directory)
