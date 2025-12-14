from turtle import*
import random
from time import*
# from Tester import*

screen = Screen()

bgcolor("Black")

#Field
speed(0)
hideturtle()
penup()
setpos(-352.5, 352.5)
pendown()
pencolor("Lime")
pensize(4)

for _ in range(4):
    fd(705)
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

#Snake
SN = Turtle()
SN.color("White")
SN.shape("square")
SN.shapesize(55/30, 55/30)
SN.penup()
headings = [90, -90, 0, 180]
SN.setheading(random.choice(headings))

x = 35/2
y = 35/2
SN.setpos(x, y)

#Movement
oe = False

speed = 1
SN.speed(speed)
state = "neutral"

def u():
    global speed, oe, state
    if oe == False:
        state = "v"
        #onkeypress(None, "Right")
        #onkeypress(None, "Down")
        #onkeypress(None, "Left")
        SN.speed(0)
        SN.setheading(90)
        SN.speed(speed)
        onkeypress(r, "Right")
        onkeypress(l, "Left")
    oe = True

def d():
    global speed, oe, state
    if oe == False:
        state = "-v"
        #onkeypress(None, "Right")
        #onkeypress(None, "Up")
        #onkeypress(None, "Left")
        SN.speed(0)
        SN.setheading(-90)
        SN.speed(speed)
        onkeypress(r, "Right")
        onkeypress(l, "Left")
    oe = True
    
def l():
    global speed, oe, state
    if oe == False:
        state = "-h"
        #onkeypress(None, "Right")
        #onkeypress(None, "Down")
        #onkeypress(None, "Up")
        SN.speed(0)
        SN.setheading(180)
        SN.speed(speed)
        onkeypress(d, "Down")
        onkeypress(u, "Up")
    oe = True

def r():
    global speed, oe, state
    if oe == False:
        state = "h"
        #onkeypress(None, "Up")
        #onkeypress(None, "Down")
        #onkeypress(None, "Left")
        SN.speed(0)
        SN.setheading(0)
        SN.speed(speed)
        onkeypress(u, "Up")
        onkeypress(d, "Down")
    oe = True

onkeypress(u, "Up")
onkeypress(d, "Down")
onkeypress(l, "Left")
onkeypress(r, "Right")
listen()

#Funcitons
n1 = 0
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

    xcor = round(SN.xcor(), 1)
    ycor = round(SN.ycor(), 1)
    if xcor == foodx and ycor == foody:
        n1 += 1
        score += 1
        foodhit = True
        speed += 1/30

n = 0
stamplist = []
stan = False

def stamps():
    global n1, n, stamplist, stan, state

    SN.stamp()
    
    if state == "h":
        co = [round(SN.xcor()-35, 1), round(SN.ycor(), 1)]
    elif state == "-h":
        co = [round(SN.xcor()+35, 1), round(SN.ycor(), 1)]
    elif state == "v":
        co = [round(SN.xcor(), 1), round(SN.ycor()-35, 1)]
    else:
        co = [round(SN.xcor(), 1), round(SN.ycor()+35, 1)]

    stamplist.append(co)

    if n1 == n:
        SN.clearstamps(1)
        stamplist.remove(stamplist[0])
        
    if n < n1:
        n += 1
        stan = True


def get_new_hsc(new_score):
    global highscore
    with open("highscore.txt", mode = "w") as hs:
        hs.write(str(new_score))
    with open("highscore.txt", mode = "r") as hs:
        hsc = hs.read()

    highscore = int(hsc)


with open("highscore.txt", mode = "r") as hs:
        hsc = hs.read()
        highscore = int(hsc)


hsc = Turtle()
hsc.hideturtle()
hsc.penup()
hsc.setpos(0, -380)
hsc.color("turquoise")
hsc.pendown()
hsc.pendown()


def wallhit():
    global st, score, highscore
    if SN.xcor() > 350-35/2 or SN.xcor() < -350+35/2 or SN.ycor() > 350-35/2 or SN.ycor() < -350+35/2:
        if SN.xcor() > 350-35/2:
            SN.speed(0)
            SN.setheading(180)
            SN.fd(700/20)
        
        if SN.xcor() < -350+35/2:
            SN.speed(0)
            SN.setheading(0)
            SN.fd(700/20)

        if SN.ycor() > 350-35/2:
            SN.speed(0)
            SN.setheading(-90)
            SN.fd(700/20)
        
        if SN.ycor() < -350+35/2:
            SN.speed(0)
            SN.setheading(90)
            SN.fd(700/20)
        
        if score > highscore:
            get_new_hsc(score)

        for _ in range(score-1):
            stamplist.remove(stamplist[0])

        hsc.undo()
        hsc.write(f"Highscore: {highscore}", align = "center", font = ("Arial", 15, "bold"))
        SN.setpos(35/2, 35/2)
        score = 0

def bodyhit():
    global stamplist, stan, score
    list = [round(SN.xcor(), 1), round(SN.ycor(), 1)]
    
    if list in stamplist and stan == False:
        #hsc.undo()
        if score > highscore:
            get_new_hsc(score)
        hsc.write(f"Highscore: {highscore}", align = "center", font = ("Arial", 15, "bold"))        
        SN.setpos(35/2, 35/2)
        score = 0
      
sc = Turtle()
sc.hideturtle()
sc.pencolor("Cyan")
sc.penup()
sc.setpos(0, 365)
sc.pendown() 
sc.pendown()

while True:
    SN.fd(700/20)
    #stamplist[-1] = None  
    oe = False
    stan = False
    foodhitf()
    stamps()
    sc.undo()
    sc.write(f"Score: {score}", align = "center", font = ("Arial", 15, "bold"))
    wallhit()
    bodyhit()
    

screen.mainloop() 












