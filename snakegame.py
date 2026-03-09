import turtle
import time 
import random
# set up screen
wn = turtle.Screen()
wn.title("snake game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) # turn off screen updates
#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"
#food
food= turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
# snake body segments
segments = []
#score
score = 0
#functions
def go_up():
    if head.direction !="down":
        head.direction="up"
def go_down():
    if head.direction !="up":
        head.direction ="down"
def go_left():
    if head.direction !="right":
        head.direction ="left"
def go_right():
    if head.direction !="left":
        head.direction="right"
def move():
    if head.direction == "up":
        y= head.ycor()
        head.sety(y+20)
    if head.direction =="down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"up")
wn.onkeypress(go_down,"down")
wn.onkeypress(go_left,"left")
wn.onkeypress(go_right,"right")
## main game loop
while True:
    wn.update()
    if head.xcor()>290 or head.xcor() < -290 or head.ycor() >290 or head.ycor <-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction ="stop"
        #hide segments 
        for segments in segments:
            segment.goto(1000,1000)
        segments.clear()
        score = 0
    if head.distance(food)<20:
       #move to food random position
       x= random.randit(-290,290)
       y= random.randit(-290,290)
       food.goto(x,y)
       # add a segment
       new_segment = turtle.Turtle()
       new_segment.speed(0)
       new_segment.shape("square")
       new_segment.color("light green")
       new_segment.penup()
       segments.append(new_segment)

       score+=10
### move the end segments first in riverse order
for index in range(len(segments) -1,0,1):
    x=segment[index -1].xcor()
    y=segment[index-1].ycor()
    segments[index].goto(x,y)
## move the segments 0 to where the head is 
if len(segments)>0:
    x =head.xcor()
    y =head.ycor()
    segments[0].goto(x,y)
## check for body collision using if statements
for segment in segments:
    if segment.distance(head)<20:
        tittle.sleep(1)
        head.goto(0,0)
        head.direction ="stop"
        for segments in segments:
            segment.goto(1000,1000)
        segments.clear()
        score = 0
move()
time.sleep(0.1) # control geme speed           