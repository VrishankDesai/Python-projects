from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # Corrected size
        self.color("blue")  # Changed to blue for better visibility
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Moves the food to a random location on the screen."""
        random_x = random.randint(-280, 280)  # Adjusted for better positioning
        random_y = random.randint(-280, 280)  # Fixed the duplicate x issue
        self.goto(random_x, random_y)
