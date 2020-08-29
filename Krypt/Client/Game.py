import pygame
from Krypt.Shared.Engine import Engine
from Krypt.Shared.Physics import World
from Krypt.Client import Scene
from Krypt.Client import Factory
from Krypt.Client.SpriteManager import SpriteManager

class Game:
    def __init__(self, user_config={}):
        defaults = {
            'width': 640,
            'height': 480,
            'scene': Scene(),
            'max_fps': 60,
            'physics': {
                'gravity': {
                    'x': 0,
                    'y': 0
                }
            }
        }
        self.__full_config = {**defaults, **user_config}
        self.width = self.__full_config['width']
        self.height = self.__full_config['height']

        pygame.init()

        self.__create_window()
        self.__setup_engine()
        self.__setup_scene(self.__full_config['scene'])
        self.__start_scene()

        pygame.quit()


    def __create_window(self):
        size = [self.width, self.height]
        self.screen = pygame.display.set_mode(size)
        # TODO: add splash screen


    def __setup_engine(self):
        max_fps = self.__full_config['max_fps']
        self.__engine = Engine(max_fps)
        self.__engine.on(Engine.PREUPDATE, self.__preupdate)
        self.__engine.on(Engine.UPDATE, self.__update)
        self.__engine.on(Engine.POSTUPDATE, self.__postupdate)


    def __setup_scene(self, scene):
        self.world = World(self.__full_config['physics'])
        sprite_manager = SpriteManager()
        factory = Factory(sprite_manager, self.world)
        self.scene = scene
        self.scene.initialize(self, factory, sprite_manager)
        self.scene.preload()
        self.scene.setup()


    def __start_scene(self):
        self.__engine.start()


    def __preupdate(self):
        self.scene.update()


    def __update(self, delta):
        self.world.update(delta)


    def __postupdate(self):
        self.scene.draw(self.screen)


    def change_scene(self, scene):
        def func():
            nonlocal self
            self.__setup_scene(scene)
            self.__start_scene()
        self.__engine.on(Engine.STOP, func, only_once=True)
        self.__engine.stop()


    def quit(self):
        self.__engine.stop()
