from turtle import Screen
from snake import Snake
from food import Food  # Import Food class
from scoreboard import Scoreboard  # Import Scoreboard class
import time

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create Game Objects
snake = Snake()
food = Food()  # Create food object
scoreboard = Scoreboard()  # Create scoreboard object

# Listen for Key Presses
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game Loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect Collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

    # Detect Collision with Wall
    if snake.head.xcor() > 288 or snake.head.xcor() < -288 or snake.head.ycor() > 288 or snake.head.ycor() < -288:
        game_is_on = False  # Stop the game
        scoreboard.game_over()  # Show game over message

screen.exitonclick()
