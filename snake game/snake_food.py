from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        snake_food_x = random.randint(-280, 280)
        snake_food_y = random.randint(-280, 280)
        self.goto(snake_food_x, snake_food_y)
        self.refresh()


    def refresh(self):
        snake_food_x = random.randint(-280, 280)
        snake_food_y = random.randint(-280, 280)
        self.goto(snake_food_x, snake_food_y)



