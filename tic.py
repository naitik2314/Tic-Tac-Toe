from turtle import Turtle

class Tic(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.horizontal_line_1()
        self.horizontal_line_2()
        self.vertical_line_1()
        self.vertical_line_2()

    def horizontal_line_1(self):
        self.penup()
        self.setheading(270)
        self.goto(-150, 300)
        self.pendown()
        self.forward(600)

    def horizontal_line_2(self):
        self.penup()
        self.setheading(270)
        self.goto(150, 300)
        self.pendown()
        self.forward(600)

    def vertical_line_1(self):
        self.penup()
        self.setheading(0)
        self.goto(-300, 150)
        self.pendown()
        self.forward(600)

    def vertical_line_2(self):
        self.penup()
        self.setheading(0)
        self.goto(-300, -150)
        self.pendown()
        self.forward(600)

    #Function to get the coordinates and send it to responsible function
    def print_position(self,x, y):
        print(f"{x}, {y}")