from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos: int, limit ,shape: str = "square", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.speed(0)
        self.penup()
        self.goto(pos, 0)
        self.color("white")
        self.shapesize(7., 1., 1.)
        self.pos = pos   
        self.limit = limit


    def moveup(self):
        # self.dy = min(self.dy + 15, 20)
        pass
        
    def movedown(self):
        # self.dy = max(self.dy - 15, -20)
        pass

    def update(self):    
        y = self.ycor() + self.dy 
        y = min(self.limit, y)
        y = max(-self.limit, y)        
        self.goto(self.pos, y)