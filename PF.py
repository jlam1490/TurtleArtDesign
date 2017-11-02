def polygonNF(t, distance, side):
    angle = 360/side
    for time in range(side):
        t.forward(distance)
        t.left(angle)

def polygon(t, distance, side):
    angle = 360/side
    t.begin_fill()
    for time in range(side):
        t.forward(distance)
        t.left(angle)
    t.end_fill()

def move(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def stripe(t,x, y):
    move(t, x, y)
    t.left(90)
    for times in range(30):
        t.color(255,255,255)
        polygon(t, 100, 4)
        t.forward(50)
    
def back(t,x ,y):
    move(t, x, y)
    for times in range(10):
        t.color(times*12, 0, times*15)
        polygon(t, 100, 4)
        t.forward(50)
        polygon(t, 100, 3)
        t.forward(50)

def background(t):
    back(t,-800, 500)
    back(t,-800, 400)
    back(t,-800, 300)
    back(t,-800, 200)
    back(t,-800, 100)
    back(t, -800, 0)
    back(t,-800, -100)
    back(t,-800, -200)
    back(t,-800, -300)
    back(t,-800, -400)
    back(t,-800, -500)
    t.right(180)
    back(t,800, 500)
    back(t,800, 400)
    back(t,800, 300)
    back(t,800, 200)
    back(t,800, 100)
    back(t,800, 0)
    back(t,800, -100)
    back(t,800, -200)
    back(t,800, -300)
    back(t,800, -400)
    back(t,800, -500)

def confetii(t, x , y):
    for times in range(100):
        move(t,x, y)
        t.color(255- times*2, 0, 255-times)
        t.forward(times+100)
        t.right(86)

    
def star(t):
    for times in range(101):
        t.color(0, 255-times*2, 255- times)
        t.begin_fill()
        t.forward(times * 4)
        t.right(587)
        t.end_fill()

def light(t):
    for times in range(250):
        t.forward(times*2)
        t.right(217)
        t.color(times, times, 255)

def chandelier(t):
    for times in range(255):
        move(t,0,400)
        t.color(0, 255, 255-times)
        t.forward(300-times)
        t.left(13)

def dome(t):
    for times in range(2):
        for times in range(29):
            t.color(255-times*3,237,255-times*2)
            polygonNF(t, 100, 15)
            t.left(37)

def treeangle(t):
    move(t,0,0)
    for times in range(150):
        move(t,0,0)
        for times in range(25):
            t.color(times*3, 0, times*4)
            polygon(t, 100, 3)
            t.left(times*10)
            t.forward(20)
        t.left(90)
        t.forward(100)
        
def together(Hi):
    from random import randint
    import turtle
    turtle.colormode(255)
    san = turtle.Turtle()
    nats = turtle.Turtle()
    brian = turtle.Turtle()
    anrew = turtle.Turtle()
    jal = turtle.Turtle()
    astel = turtle.Turtle()
    miael = turtle.Turtle()
    sabs = turtle.Turtle()
    ber = turtle.Turtle()
    astel.pensize(5)
    ber.pensize(5)
    anrew.pensize(5)
    sabs.pensize(5)
    miael.pensize(5)
    jal.pensize(5)
    brian.pensize(10)
    san.pensize(5)
    turtle.tracer(0)
    background(nats)
    for times in range(2):
        jal.left(15)
        miael.left(15)
        
        move(astel,-600,0)
        star(astel)
        
        move(ber,600,0)
        star(ber)
        
        move(miael, -800,-400)
        light(miael)    
        
        move(jal,800,-400)
        light(jal)
        
        chandelier(anrew)
        
    for times in range(2):
        dome(sabs)

    confetii(brian, 600, 400)
    confetii(brian, -600, 400)

    treeangle(san)
    
