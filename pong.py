from turtle import Turtle
from random import randint


class Pong(Turtle):

    def __init__(self, limit, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.speed(0)
        self.color("white")
        self.goto(0, 400)
        self.goto(0, -400)
        self.goto(0,-100)
        self.circle(100)
        self.penup()
        self.goto(0, 0)
        self.shape("circle")
        self.color("white")
        self.dx = randint(15, 25)
        self.dy = randint(10, 25)
        self.limit = limit

    def update(self, user, comp):
        self.check_collision(user, comp)
        if self.dx >= 0:
            self.dx = min(self.dx, 45)
        else:
            self.dx = max(self.dx, -45)
        x = self.xcor() + self.dx
        y = self.ycor() + self.dy
        if x - 40 >= user.xcor() or x + 40 <= comp.xcor():
            print("RESET: DUE TO BALL MISSED")
            self.reset()
        else:
            self.goto(x, y)
    
    def reset(self):
        self.goto(0, 0)
        self.dx = 10
        self.dy = randint(10, 25)

    def check_collision(self, user, comp):
        # check for horizontal collision first ( collision with paddle )
        if self.xcor() + 45 >= user.xcor() and (self.ycor() <= user.ycor() + 50 and self.ycor() >= user.ycor() - 50):
            self.dx *= -1
            self.dx *= 1.75
            self.dy += user.get_vel()
        elif self.xcor() - 45 <= comp.xcor() and (self.ycor() <= comp.ycor() + 50 and self.ycor() >= comp.ycor() - 50):
            self.dx *= 1.5
            self.dx *= -1
            self.dy += comp.get_vel()
            

        if self.ycor() + 15 >= self.limit or self.ycor() -15 <= -self.limit:
            self.dy *= -1