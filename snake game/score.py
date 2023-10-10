from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.user_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 17, "normal"))


    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write("GAME OVER", align="center", font=("Arial", 25, "normal"))


    def user_score(self):
        self.score += 1
        self.clear()
        self.update_score()
