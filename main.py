from turtle import *
from paddle import Paddle, Opponent
from pong import Pong
# from time import sleep



def close():
    exit(0)

screen = Screen()
screen.title("Pong Game")
screen.bgcolor("#121212")

YLIMIT = screen.window_height()//2
ball = Pong(YLIMIT)

PLAYER_POS = screen.window_width()//2 - 20
OPPONENT_POS = -PLAYER_POS -5

user = Paddle(PLAYER_POS, YLIMIT, "blue")
comp = Opponent(-PLAYER_POS, YLIMIT, "red")
screen.onkeypress(user.moveup, "Up")
screen.onkeypress(user.movedown, "Down")
screen.onkeypress(close, "s")
# computer = Paddle(OPPONENT_POS)

while True:
    screen.listen()
    user.update()
    comp.update(ball)
    ball.update(user, comp)
    screen.update()
    # sleep(0.1)
