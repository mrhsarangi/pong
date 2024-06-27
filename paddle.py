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
        self.yvel =0

    def moveup(self):
        """
            When up arrow is pressed inc upward vel
            until a max limit
        """
        self.yvel = min(self.yvel + 15, 45)
        
    def movedown(self):
        self.yvel = max(self.yvel - 15, -45)

    def update(self):    
        y = self.ycor() + self.yvel 

        if self.yvel > 0:
            self.yvel -= 5
        elif self.yvel < 0:
            self.yvel += 5

        y = min(self.limit, y)
        y = max(-self.limit, y)        
        self.goto(self.pos, y)