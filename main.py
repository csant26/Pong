"""Main module"""
import turtle
import constants as cons


class PongGame:
    """Pong game"""
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=cons.SCREEN_WIDTH,height=cons.SCREEN_HEIGHT)
        self.screen.bgcolor(cons.SCREEN_BACKGROUND_COLOR)
        self.screen.title("Pong")
        self.screen.mainloop()

pong_game = PongGame()
