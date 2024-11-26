# screen setup
import time
from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
tim = Turtle()

screen.setup(height=600, width=600)
screen.bgcolor("#2E8B57")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

tim.color("red")
tim.lt(45)
tim.penup()
tim.forward(400)
tim.setheading(180)
tim.pendown()
tim.forward(570)
tim.setheading(270)
tim.forward(570)
tim.setheading(0)
tim.forward(570)
tim.setheading(90)
tim.forward(570)
tim.hideturtle()



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.track_score()

        # detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

# detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
