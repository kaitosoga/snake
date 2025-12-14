from turtle import*

positions = [(35/2, 35/2), (35/2-35, 35/2), (35/2-35, 35/2)]

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.stamplist = []

    
    def create_snake(self):
        for pos in positions:
            self.add_segment(pos)
    
    def add_segment(self, pos):
        new_segment = Turtle("square")
        new_segment.shapesize(35/30, 35/30)
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def extend(self):
        co = self.segments[-1].pos()
        self.add_segment(co)
            
    def append(self):
        stamplist = []
        for seg in self.segments:
            stamplist.append(seg.pos)

    def move(self):
        for seg in range(len(self.segments) -1, 0, -1):
            x = self.segments[seg-1].xcor()
            y = self.segments[seg-1].ycor()
            self.segments[seg].goto(x, y)
        self.head.fd(35)

    def u(self):
        if self.head.heading() != -90:
            self.head.setheading(90)
    
    def d(self):
        if self.head.heading() != 90:
            self.head.setheading(-90)
    
    def l(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    
    def r(self):
        if self.head.heading() != 180:
            self.head.setheading(0)



    


    



