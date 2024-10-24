"""Game to practice typing.

Exercises

1. Change the speed of letters.
2. Add uppercase letters.
3. Make the game faster as the score gets higher.
4. Make the letters more frequent as the score gets higher.
"""

from random import choice, randrange
from string import ascii_lowercase
import turtle
from freegames import vector

targets = []
letters = []
score = 0


def inside(point):
    """Return True if point on screen."""
    return -200 < point.x < 200 and -200 < point.y < 200


def draw():
    """Draw letters."""
    turtle.clear()

    for target, letter in zip(targets, letters):
        turtle.goto(target.x, target.y)
        turtle.write(letter, align='center', font=('Consolas', 20, 'normal'))

    turtle.update()


def move():
    """Move letters."""
    if randrange(20) == 0:
        x = randrange(-150, 150)
        target = vector(x, 200)
        targets.append(target)
        letter = choice(ascii_lowercase)
        letters.append(letter)

    for target in targets:
        target.y -= 1

    draw()

    for target in targets:
        if not inside(target):
            return

    turtle.ontimer(move, 100)


def press(key):
    """Handle key press event."""
    global score

    if key in letters:
        score += 1
        pos = letters.index(key)
        del targets[pos]
        del letters[pos]
    else:
        score -= 1

    print('Score:', score)


# Set up the screen
turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.penup()
turtle.tracer(False)
turtle.listen()

# Bind key presses to the game logic
for letter in ascii_lowercase:
    turtle.onkey(lambda letter=letter: press(letter), letter)

move()
turtle.done()
