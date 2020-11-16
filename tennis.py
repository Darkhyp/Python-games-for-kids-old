import turtle as t
from sound import make_sound
from ball import Ball
from rocket import Rocket
import CONFIGS


class Game:
    def __init__(self):
        self.turtle_init()

        self.lrocket = Rocket('left', CONFIGS.ROCKET_SPEED, (-CONFIGS.WIDTH/2+CONFIGS.ROCKETS_DXPOS,0),CONFIGS.ROCKET1_COLOR)
        self.rrocket = Rocket('right', CONFIGS.ROCKET_SPEED, (CONFIGS.WIDTH/2-CONFIGS.ROCKETS_DXPOS,0),CONFIGS.ROCKET2_COLOR)

        self.ball = Ball(CONFIGS.BALL_SPEED,(0,0),(self.lrocket,self.rrocket))

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
        t.onkeypress(lambda: self.lrocket.deplacer_up(CONFIGS.ROCKET1_KEY_UP),CONFIGS.ROCKET1_KEY_UP)
        t.onkeypress(lambda: self.lrocket.deplacer_down(CONFIGS.ROCKET1_KEY_DOWN),CONFIGS.ROCKET1_KEY_DOWN)
        t.onkeypress(lambda: self.rrocket.deplacer_up(CONFIGS.ROCKET2_KEY_UP),CONFIGS.ROCKET2_KEY_UP)
        t.onkeypress(lambda: self.rrocket.deplacer_down(CONFIGS.ROCKET2_KEY_DOWN),CONFIGS.ROCKET2_KEY_DOWN)

        self.ball.start()
        t.mainloop()  # Place le programme en position d’attente d’une action du joueur


if __name__=='__main__':
    newgame = Game()
