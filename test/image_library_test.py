from image_library import ImageRetrievalFactory, ImageLibrary
import os
import shutil
from image import ImageMapper

test_library = 'test_image_library'

def test_init_fails_with_no_library():
    test_subject = ImageLibrary(test_library)
    remove_library()
    try:
        test_subject.init()
        raise RuntimeError("expected ImageLibraryError")
    except ImageLibrary.ImageLibraryError:
        pass

def test_init_fails_with_empty_library():
    test_subject = ImageLibrary(test_library)
    create_library()
    try:
        test_subject.init()
        raise RuntimeError("expected ImageLibraryError")
    except ImageLibrary.ImageLibraryError:
        pass
    remove_library()

def test_init_fails_with_empty_subfolders():
    test_subject = ImageLibrary(test_library)
    create_library()
    create_library_dirs()
    try:
        test_subject.init()
        raise RuntimeError("expected ImageLibraryError")
    except ImageLibrary.ImageLibraryError:
        pass
    remove_library()

def test_init_loads_file_list():
    test_subject = ImageLibrary(test_library)
    create_library()
    create_library_dirs()
    create_library_images()

    test_subject.init()

    assert isinstance(test_subject.library_files, dict)
    assert len(test_subject.library_files) == len(ImageLibrary.COLORS)

    remove_library()

def test_next_retrieves_image():
    test_subject = ImageLibrary(test_library)
    create_library()
    create_library_dirs()
    create_library_images()
    test_subject.init()

    file = test_subject.next((255, 0, 0))

    assert os.path.isfile(file)

    remove_library()

def test_next_is_cyclic():
    test_subject = ImageLibrary(test_library)
    create_library()
    create_library_dirs()
    create_library_images()
    test_subject.init()

    for i in range(0, len(test_subject.library_files['red'][1]) + 1):
        file = test_subject.next((0, 0, 0))
        assert not file is None

    remove_library()

def test_next_fails_if_not_initialized():
    test_subject = ImageLibrary(test_library)
    create_library()
    create_library_dirs()
    create_library_images()

    try:
        test_subject.next((0, 0, 0))
        raise RuntimeError("expected ImageLibraryError")
    except ImageLibrary.ImageLibraryError:
        pass

    remove_library()

def test_create_builds_library_folders():
    remove_library()
    test_subject = ImageLibrary(test_library)

    test_subject.create()
    for c in ImageLibrary.COLORS:
        assert os.path.isdir(test_library + '/' + c)

    remove_library()

def test_create_completes_even_if_library_exists():
    create_library()
    create_library_dirs()
    test_subject = ImageLibrary(test_library)

    test_subject.create()

def create_library():
    if os.path.isdir(test_library):
        remove_library()
    os.mkdir(test_library)

def create_library_dirs():
    for d in ImageLibrary.COLORS:
        if not os.path.isdir(test_library + '/' + d):
            os.mkdir(test_library + '/' + d)

def create_library_images():
    image_mapper = ImageMapper()
    for d in ImageLibrary.COLORS:
        if os.path.isdir(test_library + '/' + d):
            image_mapper.write_pixels([[(0,0,0)]],
                "{0}/{1}/image.jpg".format(test_library, d))

def remove_library():
    if os.path.isdir(test_library):
        shutil.rmtree(test_library)
