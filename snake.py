from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
COLOR = "#FFD700"
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color(COLOR)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):  # [(0, 0), (-20, 0), (-40, 0)]
            # print(f"this is seg_num: {seg_num}")
            new_x = self.segments[seg_num - 1].xcor()
            # print(f"this new_x: {new_x}")
            new_y = self.segments[seg_num - 1].ycor()
            # print(f"this new_y: {new_y}")
            self.segments[seg_num].goto(new_x, new_y)
            # print(f"this is xy: {(new_x, new_y)}")
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)



