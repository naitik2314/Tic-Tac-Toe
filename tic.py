from turtle import Turtle

class Tic(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.start = "player1"
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

    #Functions to print x and 0
    def middle_box(self):
        print("Got into the middle box")
    
    def left_to_middle_box(self):
        print("Got into left_to_middle")

    def top_left_box(self):
        print("Got to top left box")

    def bottom_left_box(self):
        print("Got to bottom left box")

    def top_to_middle(self):
        print("Got to top to middle box")

    def bottom_to_middle(self):
        print("Bottom to middle box")

    def right_to_middle(self):
        print("Right to middle box")

    def top_right_box(self):
        print("Top right box")
    
    def bottom_right_box(self):
        print("Bottom right box")

    #Function to get the coordinates and send it to responsible function
    def get_coordinates(self,x, y):
        if x < 150 and x > -150 and y < 150 and y > -150:
            self.middle_box()

        elif x < -150 and y > -150 and y < 150:
            self.left_to_middle_box()

        elif x < -150 and y > 150:
            self.top_left_box()

        elif x < -150 and y < -150:
            self.bottom_left_box()

        elif x < 150 and x > -150 and y > 150:
            self.top_to_middle()

        elif x < 150 and x > -150 and y < -150:
            self.bottom_to_middle()

        elif x > -150 and y > -150 and y < 150:
            self.right_to_middle()

        elif x > 150 and y > 150:
            self.top_right_box()
        
        elif x > 150 and y < -150:
            self.bottom_right_box()