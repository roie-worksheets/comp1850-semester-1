import sys

from image import Image, ImageError


class Binary_Image(Image):
    @classmethod
    def read_pgm_binary(cls, name):
        with open(name, 'rb') as f:
            [magic, dimensions, max_value] = map(
                lambda x: x.decode()[:-1], 
                (lines := f.readlines())[:3])
        if magic != 'P5':
            raise ImageError(f"unrecognized magic number ({magic=})")
            
        self = Binary_Image()
        self.width, self.height = map(int, dimensions.split(' '))
        self.max_value = int(max_value)
        self.pixels = list(map(int, lines[3]))
        return self

bimage = Binary_Image.read_pgm_binary(sys.argv[1]).write_pgm("raw_coins.pgm")