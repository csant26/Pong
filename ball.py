"""Setting up Ball"""
import turtle
# import math
import random
import constants as cons

class Ball(turtle.Turtle):
    """Ball"""
    def __init__(self,paddles):
        super().__init__()
        self.shape(cons.BALL_SHAPE)
        self.color(cons.BALL_COLOR)
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.dx = 2
        self.dy = 2
        self.paddles = paddles

    def move(self):
        """Move ball and bounce only if it hits a paddle"""
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

        # Bounce vertically
        if self.ycor() >= cons.MAX_BALL_YCOOR or self.ycor() <= cons.MIN_BALL_YCOOR:
            self.dy *= -1

        right_paddle = self.paddles[0]
        left_paddle = self.paddles[1]

        if self.distance(right_paddle) < 50 and self.xcor() > 340 or \
        self.distance(left_paddle) < 50 and self.xcor() < -340:
            self.dx *=-1

        # if self.xcor() >= cons.MAX_BALL_XCOOR or self.xcor() <= cons.MIN_BALL_XCOOR:
        #     self.dx *= -1
