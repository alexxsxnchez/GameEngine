from pyglet import app, graphics, gl
from pyglet.window import Window





class MyWindow:

    defined = False

    def __init__(self, width=640, height=480, title="App"):
        assert not MyWindow.defined
        MyWindow.defined = True
        self.window = Window(width=width, height=height, caption=title)

        @self.window.event
        def on_key_press(symbol, modifiers):
            self.on_key_press(symbol, modifiers)


        @self.window.event
        def on_draw():
            self.on_draw()


    def run(self):
        app.run()


    def on_key_press(self, symbol, modifiers):
        pass


    def on_key_release(self, symbol, modifiers):
        pass


    def on_draw(self):
        pass



class MyMyWindow(MyWindow):
    def __init__(self):
        super().__init__()

    def on_key_press(self, symbol, modifiers):
        print("key pressed")

    def on_draw(self):
        self.window.clear()
        graphics.draw(4, gl.GL_QUADS, ('v2f', [100, 200, 300, 200, 300, 400, 100, 400]))
        #shapes.Rectangle(x=100, y=200, width=200, height=200)



def main():
    window = MyMyWindow()
    """
    @window.event
    def on_key_press(symbol, modifiers):
        print("key press")

    app.run()
    """
    window.run()

if __name__ == '__main__':
    main()