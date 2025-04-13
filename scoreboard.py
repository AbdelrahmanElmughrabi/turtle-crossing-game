from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=0
        self.create_scoreboard()



    def create_scoreboard(self):
        self.clear()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increment_score(self):
        self.level+=1
        self.create_scoreboard()

    def gameOver(self):
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=0)
        self.write("GAMEOVER", align="Center", font=FONT)