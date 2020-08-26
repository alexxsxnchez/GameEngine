class Vec2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def __add__(self, o):
        return Vec2(self.x + o.x, self.y + o.y)


    def __sub__(self, o):
        return Vec2(self.x - o.x, self.y - o.y)


    def __mul__(self, o):
        if isinstance(o, Vec2):
            assert False
            # TODO
        else:
            # scalar multiply
            return Vec2(self.x * o, self.y * o)


    def __rmul__(self, o):
        return self.__mul__(o)


    def __neg__(self):
        return self.__mul__(-1)


    def __eq__(self, o):
        return self.x == o.x and self.y == o.y


    def __str__(self):
        return f'[{self.x}, {self.y}]'


    def round(self):
        n_digits = 5
        x = round(self.x, n_digits)
        y = round(self.y, n_digits)
        return Vec2(x, y)
