from PIL import ImageFile

class ImageParser:
    # read a given image file to an Image object
    def read(self, filename):
        file = open(filename, 'rb')
        parser = ImageFile.Parser()
        while 1:
            bytes_ = file.read(1024)
            if not bytes_:
                break
            parser.feed(bytes_)
        return parser.close().convert('RGB')
