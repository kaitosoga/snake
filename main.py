from turtle import*
import random
from time import*
from Tester import Snake

screen = Screen()

bgcolor("Black")
 
#Field
speed(0)
hideturtle()
penup()
setpos(-350, 350)
pendown()
pencolor("Lime")
pensize(4)

for _ in range(4):
    fd(700)
    rt(90)

#Start and Countdown
penup()
setpos(0, 0)
pendown()
pencolor("cyan")
write("START", align = "center", font = ("Arial", 25, "bold"))

finished = False
def goon(x, y):
    global finished
    finished = True
    Button.hideturtle()
    undo()

Button = Turtle()
Button.color("Cyan")
Button.shape("arrow")
Button.shapesize(2, 3)
Button.penup()
Button.setpos(-10, -50)

Button.onclick(fun = goon)
listen()

ti = Turtle()
ti.hideturtle()
ti.penup()

while finished == False:
    ti.fd(1)

t = 3
for _ in range (3):
    write(f"Game begins in {t} seconds", align = "center", font = ("Arial", 15, "bold"))
    sleep(1)
    undo()
    t -= 1

#snake
snake = Snake()
snake.create_snake()

#Movement
onkeypress(snake.u, "Up")
onkeypress(snake.d, "Down")
onkeypress(snake.l, "Left")
onkeypress(snake.r, "Right")
listen()

#Funcitons
meal = Turtle()
meal.hideturtle()
meal.penup()
meal.shape("circle")
meal.shapesize(0.3, 0.3)
meal.color("yellow")

score = 0
foodhit = True
cn = []
x1 = 0
for _ in range(20):
    cn.append(-350+35/2+35*x1)
    x1 += 1
foodx = 0
foody = 0

def foodhitf():
    global n1, cn, foodhit, foodx, foody, score, speed
    if foodhit == True:
        foodx = random.choice(cn)
        foody = random.choice(cn)
        meal.hideturtle()
        meal.setpos(foodx, foody)
        meal.showturtle()

        foodhit = False

    xcor = round(snake.head.xcor(), 1)
    ycor = round(snake.head.ycor(), 1)
    if xcor == foodx and ycor == foody:
        snake.extend()

def wallhit():
    global st, score
    if snake.head.xcor() > 350-35/2 or snake.head.xcor() < -350+35/2 or snake.head.ycor() > 350-35/2 or snake.head.ycor() < -350+35/2:
        if snake .head.xcor() > 350-35/2:
            snake.head.speed(0)
            snake.head.setheading(180)
            snake.head.fd(700/20)
        
        if snake.head.xcor() < -350+35/2:
            snake.head.speed(0)
            snake.head.setheading(0)
            snake.head.fd(700/20)

        if snake.head.ycor() > 350-35/2:
            snake.head.speed(0)
            snake.head.setheading(-90)
            snake.head.fd(700/20)
        
        if snake.head.ycor() < -350+35/2:
            snake.head.speed(0)
            snake.head.setheading(90)
            snake.head.fd(700/20)
        
        penup()
        setpos(0, 0)
        pendown()
        write("GAME OVER", align = "center", font = ("Arial", 40, "bold"))
        while True:
            sleep(1)

def bodyhit():
    list = [round(snake.head.xcor(), 1), round(snake.head.ycor(), 1)]
    
    if list in snake.stamplist:
        penup()
        setpos(0, 0)
        pendown()
        write("GAME OVER", align = "center", font = ("Arial", 40, "bold"))
        while True:
            sleep(1)

sc = Turtle()
sc.hideturtle()
sc.pencolor("Cyan")
sc.penup()
sc.setpos(0, 365)
sc.pendown()
sc.pendown()

while True:
    snake.move() 
    snake.append()
    foodhitf()
    sc.undo()
    sc.write(f"Score: {score}", align = "center", font = ("Arial", 15, "bold"))
    wallhit()
    bodyhit()

screen.mainloop() 





 







