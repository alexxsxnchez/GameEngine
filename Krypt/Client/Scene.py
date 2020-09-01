"""
can create sprites and sprite group
"""

import pygame
from Krypt.Shared.Physics import Factory as PhysicsFactory
from Krypt.Client import Sprite

class Factory:
    def __init__(self, sprite_manager, physics_world):
        self.__sprite_manager = sprite_manager
        self.__physics_factory = PhysicsFactory(physics_world)


    def sprite(self, x, y, width, height, image, has_physics=False, is_static=False):
        body = None
        if has_physics:
            body = self.__physics_factory.AABB(x, y, x + width, y + height, is_static)
        sprite = Sprite(x, y, width, height, image, self.__sprite_manager, body)
        self.__sprite_manager.add(sprite)
        return sprite


    def collider(self, a, b, callback=None, enable_collision=True):
        assert isinstance(a, Sprite)
        assert isinstance(b, Sprite)
        assert a.body and b.body
        return self.__physics_factory.collider(a.body, b.body, callback=callback, enable_collision=enable_collision)


    def sprite_group(self):
        pass # create sprite group


    def remove_sprite(self, sprite):
        self.__sprite_manager.remove(sprite)
        #self.__physics_factory.remove(sprite.body)


class Scene:
    def __init__(self):
        self.__game = None
        self.factory = None
        self.__sprite_manager = None


    """
    Users are meant to override this class
    """
    def initialize(self, game, factory, sprite_manager):
        """
        Users should not call this method
        """
        self.__game = game
        self.factory = factory
        self.__sprite_manager = sprite_manager


    def preload(self):
        """
        Users should override this method. Meant for loading assets.
        """


    def setup(self):
        """
        Users should override this method. Called before scene begins.
        """


    def update(self):
        """
        Users should override this method. Called before every engine renders every frame
        """


    def load(self, asset, key=None, alpha=False):
        print("loading asset")
        if not key:
            key = asset
        image = None
        if alpha:
            image = pygame.image.load(asset).convert_alpha()
        else:
            image = pygame.image.load(asset).convert()
        self.__sprite_manager.surface_cache[key] = image


    def draw(self, screen):
        # print("drawing")
        dirty_rects = []
        screen.fill((0, 0, 0))
        for sprite in self.__sprite_manager.sprites():
            sprite.draw(screen)
        #for sprite in self.__sprite_manager.get_sprites_to_draw():
        #    sprite.draw()
        # TODO: optimize what exactly is drawn
        pygame.display.flip()
        self.__sprite_manager.clear_updated()


    def change_scene(self, scene):
        self.__game.change_scene(scene)


    def stop(self):
        self.__game.quit()
