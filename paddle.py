from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos: int, limit , color: str,shape: str = "square", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.speed(0)
        self.penup()
        self.goto(pos, 0)
        self.color(color)
        self.shapesize(7., 1., 1.)
        self.xpsn = pos   
        self.limit = limit
        self.yvel =0


    def get_vel(self):
        return self.yvel

    def moveup(self):
        """
            When up arrow is pressed inc upward vel
            until a max limit
        """
        self.yvel = min(self.yvel + 30, 45)
        
    def movedown(self):
        self.yvel = max(self.yvel - 30, -45)

    def update(self):    
        y = self.ycor() + self.yvel 

        if self.yvel > 0:
            self.yvel -= 5
        elif self.yvel < 0:
            self.yvel += 5

        y = min(self.limit, y)
        y = max(-self.limit, y)        
        self.goto(self.xpsn, y)


class Opponent(Paddle):
    def update(self, ball):
        if ball.ycor() >= self.ycor() + 60:
            # move up
            self.goto(self.xpsn, self.ycor() + 30)
        elif ball.ycor() <= self.ycor() - 60:
            #move duwn
            self.goto(self.xpsn, self.ycor() - 30)
