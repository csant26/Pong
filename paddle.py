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
        self.shapesize(stretch_wid=cons.PADDLE_STRETCH_WIDTH,stretch_len=1)

    def move_paddle_up(self):
        """Moves paddle up"""
        new_y = self.ycor() + cons.PADDLE_PACE
        if new_y > cons.PADDLE_MAX_YCOOR:
            new_y = cons.PADDLE_MAX_YCOOR
        self.sety(new_y)

    def move_paddle_down(self):
        """Moves paddle down"""
        new_y = self.ycor() - cons.PADDLE_PACE
        if new_y < cons.PADDLE_MIN_YCOOR:
            new_y = cons.PADDLE_MIN_YCOOR
        self.sety(new_y)


