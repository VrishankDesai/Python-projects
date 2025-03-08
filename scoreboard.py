from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()  # Initialize the scoreboard

    def update_scoreboard(self):
        """Clears the old score and updates the scoreboard."""
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Displays 'GAME OVER' at the center of the screen."""
        self.goto(0, 0)  # Move to the center
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases the score and updates the display."""
        self.score += 1
        self.update_scoreboard()  # Clear and rewrite the score
