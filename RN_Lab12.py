from patterns import *


class Pattern:
    def __init__(self, data):
        self.data = data

    def make_image(self, filename):
        height = len(self.data)
        width = len(self.data[0])
        with open(filename, 'w') as f:
            f.write(f"P2 {width} {height} 255\n")
            for row in self.data:
                f.write(" ".join(str(val) for val in row) + " \n")
