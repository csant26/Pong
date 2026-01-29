"""Setting up Ball"""
import turtle
# import math
import random
import constants as cons

class Ball(turtle.Turtle):
    """Ball"""
    def __init__(self):
        super().__init__()
        self.shape(cons.BALL_SHAPE)
        self.color(cons.BALL_COLOR)
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.dx = cons.BALL_PACE
        self.dy = cons.BALL_PACE

    def move(self):
        """Move ball and bounce only if it hits a paddle"""
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    # def move(self,x,y):
    #      """Move ball and bounce only if it hits a paddle"""
    #      self.goto(self.xcor() + x, self.ycor() + y)

    def bounce_y(self):
        """Bounce vertically"""
        self.dy *= -1

    def bounce_x(self):
        """"Bounce horizontally"""
        self.dx *=-1
    
    def reset_position(self):
        """Reset ball position afte collision with paddle"""
        self.goto(0,0)
        self.bounce_x()
