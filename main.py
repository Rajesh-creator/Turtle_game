# import all relevant modules
import turtle
import random
import time

# Setting up a screen for our game
screen = turtle.Screen()
screen.bgcolor('lightgreen')

player_one = turtle.Turtle()
player_one.color('blue')
player_one.shape('turtle')

player_two = player_one.clone()
player_one.color('red')

player_one.penup()
player_one.goto(-300, 150)
player_two.penup()
player_two.goto(-300, -100)

player_one.goto(300, -100)
player_one.left(90)
player_one.pendown()
player_one.color('black')
player_one.forward(250)
player_one.write('Finish!', font=24)
player_one.penup()
player_one.color('red')
player_one.goto(-300, 150)
player_one.right(90)

player_one.pendown()
player_two.pendown()

die = [1, 2, 3, 4, 5, 6]

for i in range(30):
    if player_one.position() >= (300, 150):
        print('Player One wins the race')
        break

    elif player_two.position() >= (300, -100):
        print('Player Two wins the race')
        break
    else:
        die_roll = random.choice(die)
        player_one.forward(30 * die_roll)
        time.sleep(1)
        die_roll2 = random.choice(die)
        player_two.forward(30 * die_roll2)
        time.sleep(1)


# This keeps the turtle drawing on the screen
# turtle.done()

