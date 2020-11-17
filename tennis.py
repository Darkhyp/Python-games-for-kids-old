import time
import turtle as t
from sound import make_sound
from ball import Ball
from rocket import Rocket
import CONFIGS


class Game:
    def __init__(self):
        self.turtle_init()

        self.left_rocket = Rocket('left', CONFIGS.ROCKET_SPEED, (-CONFIGS.WIDTH/2+CONFIGS.ROCKETS_DXPOS,0),CONFIGS.ROCKET1_COLOR)
        self.right_rocket = Rocket('right', CONFIGS.ROCKET_SPEED, (CONFIGS.WIDTH/2-CONFIGS.ROCKETS_DXPOS,0),CONFIGS.ROCKET2_COLOR)

        self.ball = Ball(CONFIGS.BALL_SPEED,(0,0),(self.left_rocket,self.right_rocket))
        self.message_turtle = None

        t.update()
        make_sound(4)
        self.activate_keys()

    def turtle_init(self):
        t.title("Game - Tennis")
        # t.speed(0)
        t.tracer(0, 0)
        t.hideturtle()
        t.bgcolor(CONFIGS.BGCOLOR)
        t.setup(height=CONFIGS.HEIGHT,width=CONFIGS.WIDTH)

    def activate_keys(self):
        t.listen()  # Déclenche l’écoute du clavier
        # Associe à une touche a une fonction:
        t.onkeypress(lambda: self.left_rocket.deplacer_up(CONFIGS.ROCKET1_KEY_UP),CONFIGS.ROCKET1_KEY_UP)
        t.onkeypress(lambda: self.left_rocket.deplacer_down(CONFIGS.ROCKET1_KEY_DOWN),CONFIGS.ROCKET1_KEY_DOWN)
        t.onkeypress(lambda: self.right_rocket.deplacer_up(CONFIGS.ROCKET2_KEY_UP),CONFIGS.ROCKET2_KEY_UP)
        t.onkeypress(lambda: self.right_rocket.deplacer_down(CONFIGS.ROCKET2_KEY_DOWN),CONFIGS.ROCKET2_KEY_DOWN)
        t.onkeypress(lambda: self.pause(),CONFIGS.PAUSE_KEY)
        t.onkeypress(lambda: self.restart(),CONFIGS.RESTART_KEY)

        self.ball.start()
        t.mainloop()  # Place le programme en position d’attente d’une action du joueur
    def pause(self):
        self.ball.isPause = not self.ball.isPause
        if self.ball.isPause:
            self.print_message('Pause')
        else:
            self.message_turtle.clear()

    def restart(self):
        self.right_rocket.score = self.left_rocket.score = 0
        self.ball.x = 0
        self.ball.y = 0
        self.ball.printscore()
        self.ball.move()
        t.update()
        self.print_message('Restart game')

        time.sleep(1)
        self.message_turtle.clear()

    def print_message(self,msg):
        self.message_turtle = t.Turtle()
        self.message_turtle.hideturtle()
        self.message_turtle.penup()
        self.message_turtle.color(CONFIGS.MESSAGE_COLOR)
        style = ('Arial', 14, 'bold')
        self.message_turtle.setposition(0, 0)
        self.message_turtle.write(msg, font=style, align='center')

if __name__=='__main__':
    newgame = Game()
