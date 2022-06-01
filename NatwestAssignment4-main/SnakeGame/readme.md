# `SNAKE GAME IN PYTHON`
## GLOSSARY
1. Turtle : It is a pre-installed library in python which is used for creating shapes, picture, and game.

2. Time : It is used for counting the number of seconds elapsed since the epoch.

3. Random : This module is used to generate random numbers in python using the random module.

4. penup() : It stops drawing of the turtle pen.

5. speed() : It is an integer value in the range 0 to 10. So, 0 is fastest, 10 is fast, 6 is normal, 3 is slow, and 1 is slowest. If no argument is given, returns the current speed.

6. color() : It returns or set pen color and fill color.

7. shape() : It set turtle shape to the shape of a given name.

8. hideturtle() : It makes the turtle invisible.

9. xcor() : Return the turtle’s x coordinate.

10. ycor() : Return the turtle’s y coordinate.

---
## STEPS
### #STEP1  
Firstly, we will import all the modules into the program, and we will give the default value for the game.
```python
import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0
```
---
### #STEP2
- Now, we will create the window screen for the game, and also we will create the head of the snake and food for the snake. The score will be displayed at the header of the game.
- The function turtle.Screen() is used to create a window. In this code, our window is “wn” for the game.
- We have to give the window a name with the function “wn.title(“Snake Game”)”.
- To set the background color for the window we have used “wn.bgcolor(‘black’)”. Set the window height and width with the function “wn.setup(width=X, height=Y)”. Here, width=600 and height=600.
- The function window.tracer(0) turns off the screen updates. As, we do not need any screen updates other than the scoreboard, so it is set to 0.
- Now, we will create a snakehead, it is basically a turtle which will be a snake and it will move around.
- For creating a turtle we will use “turtle.Turtle()” and assign the name head. The head speed is set to 0 as we are just initializing and the head does not need to move.
- Let us initialize the head shape and color by using “head.shape(“circle”)” and “head.color(“green”)”.
- The function “head.penup()” makes sure that the path taken by the snake is not drawn.
- The “head.goto(0,0)” is used for snake position to be the center of the window and the direction to stop we will use head.direction = “stop”.
And “pen.write()” function is used to write the text at the current turtle position.
- We need the functionality that increases the snake body every time it touches food. So, we used arrays for this. We create an array called segments, which is initialized empty.  
```python
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High Score : 0", align="center",font=("candara", 24, "bold"))
```
---
### #STEP3
- Now, we need to define a function for each of these directions and set the head.direction to up, down, left, and right.
- After that, we will go ahead and make the snake move. So, we will define a function called move().
- If the head goes up, the “y” coordinate is increased, if the head goes down, the “y” coordinate decreases.
- If the head moves right, the “x” coordinate increases and if the head moves left, the “x” coordinate decreases.
```python
# assigning key directions
def group():
    if head.direction != "down":
        head.direction = "up"
 
 
def godown():
    if head.direction != "up":
        head.direction = "down"
 
 
def goleft():
    if head.direction != "right":
        head.direction = "left"
 
 
def goright():
    if head.direction != "left":
        head.direction = "right"
 
 
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
```
---
### #STEP4
- We will assign a key to the snake movements. By clicking the keywords, we can move the snake up, down, left, and right direction.
- We need the system to listen to our control keypress, so we will add a function called wn.listen() that listens to the key pressed.
- Every keypress needs to be bound to a function that carries out an action. We will use the function ” wn.onkeypress(function, “key”) “ for all four. Here, I have used “Up” for up, “Down” for down, “Left” for left, and “Right” for right.
- Now, we can operate the movement of a snake on the screen.
```python
wn.listen()
wn.onkeypress(goup, "Up")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "Right")
```
---
### #Step 5:
- So, now the function does nothing until it’s called. We need to call the function every time we update the screen or the window.
- We have to be sure that the snakes die when it collides with the border. We already have the coordinate of the border. So, we just need to reset the snakehead position when it touches the coordinates.
- Also, the snake needs to stop moving and hence change the direction to stop.
To slow down the snake movement we need to use the time module otherwise the default behavior for the move function is very fast.
- So, we will use the function time.sleep() to reduce turtle speed.
- The segment needs to disappear when the snake dies.
- So, now we need to set the position of the segments outside the window coordinates. The game restarts and hence clear the segment list.
- We need to add a segment to the snake body every time it touches the food. So, we have the condition that checks for the head’s collision with food.
- Create a new_segment, define its speed, shape, and color and append it to segments array.
Now, adding the segment to the snakehead is not enough. These segments need to move when the snakehead moves.
- To move the last segment which is in the position x to x-1 and x-1 to x-2 and so on.
The snake needs to die if it touches itself. So, we are going to check if the distance between the segment and head is less than 20. If it is, reset the head position and head direction.
- At last, we need to see the situation when the score increases. The first one is when the head collides with the food. Increase the score and update the high_score.
- We used pen.write() function to write the score on the screen.
- We need to reset the score when the snakehead collides with the border and with its own tail
- And then call the function time.sleep(delay) to reduce turtle speed.
```python
# Main Gameplay
segments = []
while True:
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
 
        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    # Checking for head collisions with body segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()
 
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)
 
wn.mainloop()
```