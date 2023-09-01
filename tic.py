from turtle import Turtle

class Tic(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.boxes = ["nil"]
        self.moves = 0
        self.it_has_been_skipped = False
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

    #Function to call if space is already filled
    def space_filled(self):
        self.penup()
        self.goto(0, 400)
        self.write("Box not empty, try another one", align="center", font=('Times New Roman', 12))

    #Functions to print x and 0
    def middle_box(self):
        self.penup()
        for positions_filled in self.boxes:
            if positions_filled == "middle_box":
                self.penup()
                self.goto(0, 400)
                self.write("Box not empty, try another one", align="center", font=('Times New Roman', 12))
                self.it_has_been_skipped = True

        if self.it_has_been_skipped != True:
            self.moves += 1
            self.goto(0, -75)
            if self.moves % 2 != 0:
                self.boxes.append("middle_box")
                self.write("X", align="center", font=("Arial", 100))
                self.it_has_been_skipped = False
            else:
                self.boxes.append("middle_box")
                self.write("O", align="center", font=("Arial", 100))
                self.it_has_been_skipped = False
    
    def left_to_middle_box(self):
        self.penup()
        for positions_filled in self.boxes:
            if positions_filled == "left_to_middle":
                self.penup()
                self.goto(0, 400)
                self.write("Box not empty, try another one", align="center", font=('Times New Roman', 12))
                self.it_has_been_skipped = True

        if self.it_has_been_skipped != True:
            self.moves += 1
            self.goto(-220, -75)
            if self.moves % 2 != 0:
                self.boxes.append("left_to_middle")
                self.write("X", align="center", font=("Arial", 100))
                self.it_has_been_skipped = False
            else:
                self.boxes.append("left_to_middle")
                self.write("O", align="center", font=("Arial", 100))
                self.it_has_been_skipped = False

    def top_left_box(self):
        self.penup()
        for positions_filled in self.boxes:
            if positions_filled == "top_left":
                self.penup()
                self.goto(0, 400)
                self.write("Box not empty, try another one", align="center", font=('Times New Roman', 12))
                self.it_has_been_skipped = True

        if self.it_has_been_skipped != True:
            self.moves += 1
            self.goto(-220, 150)
            if self.moves % 2 != 0:
                self.boxes.append("top_left")
                self.write("X", align="center", font=("Arial", 100))
                self.it_has_been_skipped = False
                
            else:
                self.boxes.append("top_left")
                self.write("O", align="center", font=("Arial", 100))
                self.it_has_been_skipped = False

    def bottom_left_box(self):
        self.penup()
        for positions_filled in self.boxes:
            if positions_filled == "bottom_left":
                self.penup()
                self.goto(0, 400)
                self.write("Box not empty, try another one", align="center", font=('Times New Roman', 12))
                self.it_has_been_skipped = True

        if self.it_has_been_skipped != True:
            self.moves += 1
            self.goto(-220, -300)
            if self.moves % 2 != 0:
                self.boxes.append("bottom_left")
                self.write("X", align="center", font=("Arial", 100))
                self.it_has_been_skipped = False
                
            else:
                self.boxes.append("bottom_left")
                self.write("O", align="center", font=("Arial", 100))
                self.it_has_been_skipped = False

    def top_to_middle(self):
        self.penup()
        for positions_filled in self.boxes:
            if positions_filled == "top_to_middle":
                self.penup()
                self.goto(0, 400)
                self.write("Box not empty, try another one", align="center", font=('Times New Roman', 12))
                self.it_has_been_skipped = True

        if self.it_has_been_skipped != True:
            self.moves += 1
            self.goto(0, 150)
            if self.moves % 2 != 0:
                self.boxes.append("top_to_middle")
                self.write("X", align="center", font=("Arial", 100))
                self.it_has_been_skipped = False
                
            else:
                self.boxes.append("top_to_middle")
                self.write("O", align="center", font=("Arial", 100))
                self.it_has_been_skipped = False

    def bottom_to_middle(self):
        self.penup()
        for positions_filled in self.boxes:
            if positions_filled == "bottom_to_middle":
                self.penup()
                self.goto(0, 400)
                self.write("Box not empty, try another one", align="center", font=('Times New Roman', 12))
                self.it_has_been_skipped = True

        if self.it_has_been_skipped != True:
            self.moves += 1
            self.goto(0, -300)
            if self.moves % 2 != 0:
                self.boxes.append("bottom_to_middle")
                self.write("X", align="center", font=("Arial", 100))
                self.it_has_been_skipped = False
                
            else:
                self.boxes.append("bottom_to_middle")
                self.write("O", align="center", font=("Arial", 100))
                self.it_has_been_skipped = False

    def right_to_middle(self):
        self.penup()
        for positions_filled in self.boxes:
            if positions_filled == "right_to_middle":
                self.penup()
                self.goto(0, 400)
                self.write("Box not empty, try another one", align="center", font=('Times New Roman', 12))
                self.it_has_been_skipped = True

        if self.it_has_been_skipped != True:
            self.moves += 1
            self.goto(220, -75)
            if self.moves % 2 != 0:
                self.boxes.append("right_to_middle")
                self.write("X", align="center", font=("Arial", 100))
                self.it_has_been_skipped = False
                
            else:
                self.boxes.append("right_to_middle")
                self.write("O", align="center", font=("Arial", 100))
                self.it_has_been_skipped = False

    def top_right_box(self):
        self.penup()
        for positions_filled in self.boxes:
            if positions_filled == "top_right_box":
                self.penup()
                self.goto(0, 400)
                self.write("Box not empty, try another one", align="center", font=('Times New Roman', 12))
                self.it_has_been_skipped = True

        if self.it_has_been_skipped != True:
            self.moves += 1
            self.goto(220, 150)
            if self.moves % 2 != 0:
                self.boxes.append("top_right_box")
                self.write("X", align="center", font=("Arial", 100))
                self.it_has_been_skipped = False
                
            else:
                self.boxes.append("top_right_box")
                self.write("O", align="center", font=("Arial", 100))
                self.it_has_been_skipped = False
    
    def bottom_right_box(self):
        self.penup()
        for positions_filled in self.boxes:
            if positions_filled == "bottom_right_box":
                self.penup()
                self.goto(0, 400)
                self.write("Box not empty, try another one", align="center", font=('Times New Roman', 12))
                self.it_has_been_skipped = True

        if self.it_has_been_skipped != True:
            self.moves += 1
            self.goto(220, -300)
            if self.moves % 2 != 0:
                self.boxes.append("bottom_right_box")
                self.write("X", align="center", font=("Arial", 100))
                self.it_has_been_skipped = False
                
            else:
                self.boxes.append("bottom_right_box")
                self.write("O", align="center", font=("Arial", 100))
                self.it_has_been_skipped = False

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