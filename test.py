import arcade

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Welcome to Arcade"
RADIUS = 150

class Window(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.setup()


    def setup(self):
        print("LOOOO")
        # Set the background color
        arcade.set_background_color(arcade.color.WHITE)
        self.all_sprites = arcade.SpriteList()
        # Set up the player
        self.player = arcade.Sprite("assets/bomb.png")
        self.player.center_y = self.height / 2
        self.player.left = 10
        self.all_sprites.append(self.player)


    def on_key_press(self, symbol, modifiers):
        """Handle user keyboard input
        Q: Quit the game
        P: Pause/Unpause the game
        I/J/K/L: Move Up, Left, Down, Right
        Arrows: Move Up, Left, Down, Right

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()
        """
        if symbol == arcade.key.P:
            self.paused = not self.paused
        """
        if symbol == arcade.key.I or symbol == arcade.key.UP:
            self.player.center_y += 5

        if symbol == arcade.key.K or symbol == arcade.key.DOWN:
            self.player.center_y += -5

        if symbol == arcade.key.J or symbol == arcade.key.LEFT:
            self.player.center_x += -5

        if symbol == arcade.key.L or symbol == arcade.key.RIGHT:
            self.player.center_x += 5


    def on_draw(self):
        self.all_sprites.update()
        # Clear the screen and start drawing
        arcade.start_render()
        self.all_sprites.draw()


def main():
    Window()
    arcade.run()


if __name__ == "__main__":
    main()
