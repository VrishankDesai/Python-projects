from turtle import Turtle

# Constants
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the initial snake with three segments."""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a new segment at the given position."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Extends the snake by adding a new segment at the tail's position."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves the snake forward."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Changes direction to UP unless moving DOWN."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Changes direction to DOWN unless moving UP."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Changes direction to LEFT unless moving RIGHT."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Changes direction to RIGHT unless moving LEFT."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        """Resets the snake to the starting position."""
        for segment in self.segments:
            segment.goto(1000, 1000)  # Move old segments off-screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
