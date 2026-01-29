"""Setting up Paddle"""
import turtle
import constants as cons
class Paddle(turtle.Turtle):
    """Paddle"""
    def __init__(self):
        super().__init__()
        self.shape(cons.PADDLE_SHAPE)
        self.color(cons.PADDLE_COLOUR)
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
