from image_library import ImageLibrary

testSubject = ImageLibrary.ColorMapper()

def test_name_exact_value_red():
    assert 'red' == testSubject.name((255, 0, 0))

def test_name_exact_value_brown():
    assert 'brown' == testSubject.name((150, 75, 0))

def test_name_closest_value_red():
    expected = 'red'
    assert expected == testSubject.name((200, 0, 0))
    assert expected == testSubject.name((255, 10, 0))
    assert expected == testSubject.name((185, 0, 20))
