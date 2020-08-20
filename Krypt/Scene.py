from Krypt.Physics import Factory as PhysicsFactory
from Krypt import Sprite

"""
can create sprites and sprite group
"""

class Factory:
    def __init__(self, sprites, physics_world):
        self.sprites = sprites
        self.physics_factory = PhysicsFactory(physics_world)

    def sprite(self, x, y, width, height, has_physics=False, is_static=False):
        pass # create sprite


    def sprite_group(self):
        pass # create sprite group


class Scene:
    def __init__(self):
        pass

    """
    Users are meant to override this class
    """
    def initialize(self, game, physics_world):
        """
        Users should not call this method
        """
        print("initializing scene")
        self.__game = game
        self.sprites = []
        self.factory = Factory(self.sprites, physics_world)


    def preload(self):
        """
        Users should override this method. Meant for loading assets.
        """
        pass


    def setup(self):
        """
        Users should override this method. Called before scene begins.
        """
        pass


    def update(self):
        """
        Users should override this method. Called before every engine renders every frame
        """
        pass


    def load(self, asset):
        print("loading asset")
        pass


    def draw(self):
        print("drawing")
        for sprite in self.sprites:
            sprite.draw()


    def stop(self):
        self.__game.quit()
