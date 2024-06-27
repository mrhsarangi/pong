from turtle import *
from paddle import Paddle
from pong import Pong


ball = Pong()

screen = Screen()
screen.title("Pong Game")
screen.bgcolor("#121212")

YLIMIT = screen.window_height()//2

PLAYER_POS = screen.window_width()//2 - 20
OPPONENT_POS = -PLAYER_POS -5

user = Paddle(PLAYER_POS, YLIMIT)
screen.onkeypress(user.moveup, "Up")
screen.onkeypress(user.movedown, "Down")
# computer = Paddle(OPPONENT_POS)

while True:
    screen.listen()
    user.update()
    screen.update()