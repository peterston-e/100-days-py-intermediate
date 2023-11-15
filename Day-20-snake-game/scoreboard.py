from turtle import Turtle
FONT = ("Courier", 18, "normal")
ALIGNMENT = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over.", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
