from turtle import Turtle


class Pong(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
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
        self.color("red")

        self.dx = 0
        self.dy = 0
