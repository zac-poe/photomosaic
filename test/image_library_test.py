from image_library import ImageLibrary
import os
import shutil
from image import ImageMapper

test_library = 'test_image_library'
test_subject = ImageLibrary(test_library)

def test_validate_fails_with_no_library():
    remove_library()
    try:
        test_subject.validate()
        raise RuntimeError("expected ImageLibraryError")
    except ImageLibrary.ImageLibraryError:
        pass

def test_validate_fails_with_empty_library():
    create_library()
    try:
        test_subject.validate()
        raise RuntimeError("expected ImageLibraryError")
    except ImageLibrary.ImageLibraryError:
        pass
    remove_library()

def test_validate_fails_with_empty_subfolders():
    create_library()
    create_library_dirs()
    try:
        test_subject.validate()
        raise RuntimeError("expected ImageLibraryError")
    except ImageLibrary.ImageLibraryError:
        pass
    remove_library()

def test_validate_success():
    create_library()
    create_library_dirs()
    create_library_images()

    test_subject.validate()

    remove_library()

def create_library():
    if os.path.isdir(test_library):
        remove_library()
    os.mkdir(test_library)

def create_library_dirs():
    for d in ImageLibrary.ColorMapper.COLOR_SPECTRUM:
        if not os.path.isdir(test_library + '/' + d):
            os.mkdir(test_library + '/' + d)

def create_library_images():
    image_mapper = ImageMapper()
    for d in ImageLibrary.ColorMapper.COLOR_SPECTRUM:
        if os.path.isdir(test_library + '/' + d):
            image_mapper.write_pixels([[(0,0,0)]],
                "{0}/{1}/image.jpg".format(test_library, d))

def remove_library():
    if os.path.isdir(test_library):
        shutil.rmtree(test_library)
