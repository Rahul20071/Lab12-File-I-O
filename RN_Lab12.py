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
class Rings(Pattern):
    def __init__(self, size):
        data = []
        cx, cy = size // 2, size // 2
        for y in range(size):
            row = []
            for x in range(size):
                dist = int(((x - cx)**2 + (y - cy)**2) ** 0.5)
                if dist % 20 < 10:
                    row.append(0)
                else:
                    row.append(255)
            data.append(row)
        super().__init__(data)

class DiagonalStripes(Pattern):
    def __init__(self, size, stripe_width):
        data = []
        for y in range(size):
            row = []
            for x in range(size):
                if ((x + y) // stripe_width) % 2 == 0:
                    row.append(0)
                else:
                    row.append(255)
            data.append(row)
        super().__init__(data)

class RadialGradient(Pattern):
    def __init__(self, size):
        data = []
        cx, cy = size // 2, size // 2
        max_dist = ((cx**2 + cy**2) ** 0.5)
        for y in range(size):
            row = []
            for x in range(size):
                dist = ((x - cx)**2 + (y - cy)**2) ** 0.5
                value = int(dist / max_dist * 255)
                row.append(value)
            data.append(row)
        super().__init__(data)

if __name__ == "__main__":
    pattern_data = Pattern([[0, 64, 128, 192, 255],[0, 64, 128, 192, 255]])
    pattern_data.make_image("image.pgm")
    Rings(100).make_image("rings.pgm")
    DiagonalStripes(100, 10).make_image("stripes.pgm")
    RadialGradient(100).make_image("radial.pgm")