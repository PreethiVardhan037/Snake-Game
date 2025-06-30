from turtle import Turtle
ALIGNMENT_OF_SCORE = "center"
ALIGNMENT_OF_LIVES = "right"
FONT = ("Courier New", 24, "bold")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=-225, y=270)
        self.score = 0
        self.update_score()
    def game_over(self):
        self.goto(x=0,y=0)
        self.write("GAME OVER",align=ALIGNMENT_OF_SCORE,font=FONT)
    def update_score(self):
        """updates score every time the serpent catches the food."""
        self.clear()
        self.write(arg=f"score: {self.score} ", align=ALIGNMENT_OF_SCORE, font=FONT)
        self.score += 1
class LivesBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=225,y=270)
        self.lives = 3
        self.update_lives()
    def update_lives(self):
        self.clear()
        self.write(arg=f"Lives:{self.lives}",align=ALIGNMENT_OF_LIVES,font=FONT)
        self.lives -= 1






