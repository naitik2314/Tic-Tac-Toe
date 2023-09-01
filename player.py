from turtle import Turtle

class Player(Turtle):
    def __init__(self, name, position):
        super().__init__()
        self.position = position
        self.name = name
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.write_player_name()

    def write_player_name(self):
        self.write(self.name, align='left', font=('Comic Sans MS', 15, "normal"))