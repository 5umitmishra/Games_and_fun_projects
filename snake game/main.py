from turtle import Screen
import time
from snake import Snake
from snake_food import Food
from score import ScoreBoard

screen = Screen()

screen.setup(width=600, height=600 )
screen.bgcolor("black")

screen.title("my snake game")
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.user_score()

    if snake.head.xcor() > 280 or snake.head. xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()





















