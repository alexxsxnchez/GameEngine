class Vec2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, o):
        return Vec2(self.x + o.x, self.y + o.y)

    def __sub__(self, o):
        return Vec2(self.x - o.x, self.y - o.y)

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

    def __str__(self):
        return f'[{self.x}, {self.y}]'
