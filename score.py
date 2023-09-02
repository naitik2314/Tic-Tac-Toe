from turtle import Turtle

class Score(Turtle):
    def __init__(self, number_of_games, position, name):
        super().__init__()
        self.max_score = number_of_games
        self.score = 0
        self.penup()
        self.color("white")
        self.position = position
        self.hideturtle()
        self.goto(position)
        self.name = name
        self.update_scoreboard()

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(self.score, align="center", font=('Comic Sans MS', 15, "normal"))

    def winner_declaration(self):
        self.goto(0, -400)
        self.write(f"{self.name} won!", align="center", font=('Times New Roman', 20, "normal"))
