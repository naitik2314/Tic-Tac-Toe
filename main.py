from turtle import Screen
from player import Player
from score import Score
from tic import Tic
import time

from tie import Tie

def send_coordinates(x, y):
    tic.get_coordinates(x, y)

#Screen setup
screen = Screen()
screen.setup(1000, 1000)
screen.bgcolor("black")
screen.title("Tic Tac Toe")
screen.listen()
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
score1 = Score(number_of_games, (-300, 400), player1_name)
score2 = Score(number_of_games, (-300, 350), player2_name)

#Intialize the board
tic = Tic()
tie = Tie()

#Updating the screen
screen.update()

#Adding screen listen functionality
screen.onscreenclick(send_coordinates)

game_is_on = True

while game_is_on:
    #As the screen tracer is 0, we are updating the screen here
    screen.update()

    #We check for the winner
    tic.check_winner()

    #If we have a winner, we check if the intended score is reached, if not, then we reset
    if tic.winner == True:
        if tic.winner_player == 'X':
            score1.increase_score()
        elif tic.winner_player == 'O':
            score2.increase_score()
        if score1.score >= number_of_games or score2.score >= number_of_games:
            if score1.score >= number_of_games:
                score1.winner_declaration()
            else:
                score2.winner_declaration()
            game_is_on = False
        else:
            time.sleep(2)
            tic.tic_reset()

    #If the board is full, we declare a tie
    if tic.moves == 9:
        tie.tie_display()
        time.sleep(2)
        tic.tic_reset

    #We reset the it has been skipped variable
    tic.it_has_been_skipped = False

screen.exitonclick()