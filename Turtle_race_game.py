from turtle import Turtle,Screen
import random
screen = Screen()


is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
color = ["red", "orange", "yellow", "green", "blue", "purple"]

y_position = [-100, -60, -20, 20, 60, 100]
all_racing_turtle = []


for turtle_cordinates in range(0, 6):
    new_turtle = Turtle()
    new_turtle.color(color[turtle_cordinates])
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.goto(x=-230,y=y_position[turtle_cordinates])
    all_racing_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for racer in all_racing_turtle:
        if racer.xcor() > 230:
            is_race_on = False
            winning_color = racer.pencolor()
            if winning_color == user_bet:
                print(f"you,ve won! the {winning_color} turtle is win")
            else:
                print(f"you've lost! the {winning_color} turtle is win")



        random_speed = random.randint(0,10)
        racer.forward(random_speed)

screen.exitonclick()
