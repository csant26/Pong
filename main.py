"""Main module"""
import turtle
import tkinter.messagebox as msg
import constants as cons
import paddle
import ball
import scoreboard

class PongGame:
    """Pong game"""
    def __init__(self):
        self.initialize_screen()
        self.game_on = True
        self.paddles: list[paddle.Paddle] = []
        self.initialize_paddles()
        self.initialize_middle_ground()
        self.pong_ball = ball.Ball()
        self.score = scoreboard.Scoreboard()
        self.game_loop()


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
        paddle1.goto(x=cons.RIGHT_PADDLE_XCOOR,y=cons.RIGHT_PADDLE_YCOOR)
        paddle2.goto(x=cons.LEFT_PADDLE_XCOOR,y=cons.LEFT_PADDLE_YCOOR)
        self.paddles.extend([paddle1,paddle2])
        self.initialize_paddle_motion()

    def initialize_paddle_motion(self):
        """Initialize paddle motion through key listen"""
        self.screen.listen()
        self.screen.onkey(self.paddles[0].move_paddle_up,"Up")
        self.screen.onkey(self.paddles[0].move_paddle_down,"Down")
        self.screen.onkey(self.paddles[1].move_paddle_up,"w")
        self.screen.onkey(self.paddles[1].move_paddle_down,"s")

    def initialize_middle_ground(self):
        """Creates a dashed line that separates the paddles"""
        middle_ground = turtle.Turtle()
        middle_ground.color("white")
        middle_ground.penup()
        middle_ground.goto(x=0,y=cons.MAX_SCREEN_YCOOR)
        middle_ground.setheading(270)
        middle_ground.pendown()
        while middle_ground.ycor() != cons.MIN_SCREEN_YCOOR:
            middle_ground.forward(cons.MIDDLE_SPACE)
            middle_ground.penup()
            middle_ground.forward(cons.MIDDLE_SPACE)
            middle_ground.pendown()

    def game_loop(self):
        """Runs Pong on loop"""
        if not self.game_on:
            self.screen.bye()
            return

        self.pong_ball.move()

        if self.pong_ball.ycor() >= cons.MAX_BALL_YCOOR or \
            self.pong_ball.ycor() <= cons.MIN_BALL_YCOOR:
            self.pong_ball.bounce_y()

        right_paddle = self.paddles[0]
        left_paddle = self.paddles[1]

        if self.pong_ball.distance(right_paddle) < 50 and self.pong_ball.xcor() > 340 or \
        self.pong_ball.distance(left_paddle) < 50 and self.pong_ball.xcor() < -340:
            self.pong_ball.bounce_x()

        if self.pong_ball.xcor() > 360:
            self.score.left_point()
            self.pong_ball.reset_position()
        
        if self.pong_ball.xcor() < -360:
            self.score.right_point()
            self.pong_ball.reset_position()
        
        (is_final,winner) = self.score.has_reached_finale()
        if is_final:
            msg.showinfo("WINNER",f"{winner} has won the game.")
            self.game_on = False

        self.screen.update()
        self.screen.ontimer(self.game_loop,16)

    def run(self):
        """Run Pong"""
        self.game_loop()
        self.screen.mainloop()


pong_game = PongGame()
pong_game.run()
