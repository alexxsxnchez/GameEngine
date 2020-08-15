from Physics.Vec2 import Vec2

class World:
    def __init__(self):
        print('created world')
        v1 = Vec2(1, 4)
        v2 = Vec2(2, - 5)
        print(v1 - v2)

    def update(self):
        print('world updating')
