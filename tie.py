from turtle import Turtle

class Tie(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, -400)
    
    def tie_display(self):
        self.clear()
        self.write("It is a tie", align="center", font=('Times New Roman', 20, "normal"))