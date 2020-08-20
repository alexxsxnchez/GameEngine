import pygame
from Krypt.Engine import Engine
from Krypt import Scene

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

        pygame.init()

        self.__create_window()
        self.__setup_game()
        self.__start_game()
        
        pygame.quit()


    def __create_window(self):
        size = [self.__full_config['width'], self.__full_config['height']]
        self.screen = pygame.display.set_mode(size)
        # TODO: add splash screen


    def __setup_game(self):
        self.__engine = Engine(self.__full_config['max_fps'], self.__full_config['physics'])
        self.__engine.on(Engine.PREUPDATE, self.__preupdate)
        self.__engine.on(Engine.POSTUPDATE, self.__postupdate)
        self.scene = self.__full_config['scene']
        self.scene.initialize(self, self.__engine.world)
        self.scene.preload()


    def __start_game(self):
        self.scene.setup()
        self.__engine.start()        


    def __preupdate(self):
        self.scene.update()


    def __postupdate(self):
        self.scene.draw()


    def quit(self):
        self.__engine.stop()
