"""Main module"""
import turtle
import constants as cons
import paddle


class PongGame:
    """Pong game"""
    def __init__(self):
        self.initialize_screen()
        self.paddles: list[paddle.Paddle] = []
        self.initialize_paddles()
        self.screen.update()
        self.screen.exitonclick()

    def initialize_screen(self):
        """Initialize Pong screen"""
        self.screen = turtle.Screen()
        self.screen.setup(width=cons.SCREEN_WIDTH,height=cons.SCREEN_HEIGHT)
        self.screen.bgcolor(cons.SCREEN_BACKGROUND_COLOR)
        self.screen.title("Pong")
        self.screen.tracer(0)

    def initialize_paddles(self):
        """Initiliazes paddles"""
        paddle1 = paddle.Paddle()
        paddle2 = paddle.Paddle()
        paddle1.goto(x=cons.FIRST_PADDLE_XCOOR,y=cons.FIRST_PADDLE_YCOOR)
        paddle2.goto(x=cons.SECOND_PADDLE_XCOOR,y=cons.SECOND_PADDLE_YCOOR)

pong_game = PongGame()
