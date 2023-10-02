from turtle import Turtle, Screen
screen = Screen()


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)
        screen.listen()

    def move_up(self):
        ycor = self.ycor() + 20
        self.penup()
        self.goto(self.xcor(), ycor)

    def move_down(self):
        ycor = self.ycor() - 20
        self.penup()
        self.goto(self.xcor(), ycor)
