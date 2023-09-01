from turtle import Screen
from player import Player
from score import Score
from tic import Tic

#Screen setup
screen = Screen()
screen.setup(1000, 1000)
screen.bgcolor("black")
screen.title("Tic Tac Toe")
screen.tracer(0)

#Taking number of games inputs
number_of_games = screen.numinput("Max Score", "Enter score", default=5, minval=3, maxval=10)

#Taking player names
player1_name = screen.textinput("Enter player 1 name", "Enter name")
player2_name = screen.textinput("Enter player 2 name", "Enter name")

#Initialize Players
player1 = Player(player1_name, (-450, 400))
player2 = Player(player2_name, (-450, 350))

#Initialize the Scoreboard
score1 = Score(number_of_games, (-300, 400))
score2 = Score(number_of_games, (-300, 350))

#Intialize the board
tic = Tic()

#Updating the screen
screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    if score1.score > number_of_games or score2.score > number_of_games:
        game_is_on = False

screen.exitonclick()