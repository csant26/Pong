"""Main module"""
import turtle
import constants as cons
import paddle


class PongGame:
    """Pong game"""
    def __init__(self):
        self.initialize_screen()
        self.game_on = True
        self.paddles: list[paddle.Paddle] = []
        self.initialize_paddles()
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
        paddle1.goto(x=cons.FIRST_PADDLE_XCOOR,y=cons.FIRST_PADDLE_YCOOR)
        paddle2.goto(x=cons.SECOND_PADDLE_XCOOR,y=cons.SECOND_PADDLE_YCOOR)
        self.paddles.extend([paddle1,paddle2])
        self.initialize_paddle_motion()

    def initialize_paddle_motion(self):
        """Initialize paddle motion through key listen"""
        self.screen.listen()
        self.screen.onkey(self.paddles[0].move_paddle_up,"Up")
        self.screen.onkey(self.paddles[0].move_paddle_down,"Down")
        self.screen.onkey(self.paddles[1].move_paddle_up,"w")
        self.screen.onkey(self.paddles[1].move_paddle_down,"s")

    def game_loop(self):
        """Runs Pong on loop"""
        if not self.game_on:
            return
        self.screen.update()
        self.screen.ontimer(self.game_loop,16)

    def run(self):
        """Run Pong"""
        self.game_loop()
        self.screen.mainloop()


pong_game = PongGame()
pong_game.run()
