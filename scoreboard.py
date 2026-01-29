"""Setting up scoreboard"""

import turtle
import constants as cons

class Scoreboard(turtle.Turtle):
    """Scoreboard"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(cons.SCORE_COLOR)
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scores"""
        self.clear()
        self.goto(-100,200)
        self.write(self.left_score,align="center",font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.right_score,align="center",font=("Courier",80,"normal"))

    def left_point(self):
        """Gives left player point"""
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        """Gives right player point"""
        self.right_score += 1
        self.update_scoreboard()

    def has_reached_finale(self):
        """finds out if game has winner and who"""
        if self.left_score > cons.WINNING_SCORE or self.right_score > cons.WINNING_SCORE:
            winner = "Left" if self.left_score > cons.WINNING_SCORE else "Right"
            return True, winner
        return False, ""
