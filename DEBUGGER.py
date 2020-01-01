import turtle,random,time,winsound

#for create player's rock for crash bug
def rock(color,x,y,ply):
    ply.shape("square")
    ply.shapesize(2,4)
    ply.color(color)
    ply.speed(1000)
    ply.penup()
    ply.setpos(x,y)
    ply.pendown()
    

def random_bug(size,dot):
    x= random.randint(-300,300)
    y= -350
    color=['red','pink','blue','orange','purple','yellow','cyan','green']
    dot.speed(random.randint(5,10))    
    dot.shapesize(size)
    dot.color(random.choice(color))
    dot.shape("turtle")
    dot.penup()
    dot.ht()
    winsound.PlaySound("soundBug.wav",winsound.SND_ASYNC)
    dot.setpos(x,y)
    dot.st()
    #for control distance, hide bug and record score
    while(1):
        if  dot.ycor() > ply1.ycor()-50 and dot.ycor() < ply1.ycor()+50 and dot.xcor()<ply1.xcor()+20 and dot.xcor()>ply1.xcor()-20  :
            dot.ht()
            global xp1
            xp1 += 1
            winsound.PlaySound("soundY.wav",winsound.SND_ASYNC)
            scorboard()
            break
        
        if  dot.ycor() > ply2.ycor()-50 and dot.ycor() < ply2.ycor()+50 and dot.xcor()<ply2.xcor()+20 and dot.xcor()>ply2.xcor()-20  :
            dot.ht()
            global xp2
            xp2 += 1
            winsound.PlaySound("soundC.wav",winsound.SND_ASYNC)
            scorboard()
            break
        else:
            if x<0:
                dot.forward(1.5)
            if dot.xcor()>501:
                break
            if x>0:
                dot.backward(1.5)
            if dot.xcor()<-501:
                break
    dot.pendown()
    dot.clear()

#purple borders
def sınır(lim,color):
    lim.color(color)
    lim.speed(500)
    lim.penup()
    lim.setpos(2000,350)
    lim.pendown()
    lim.setpos(-2000,350)
    lim.penup()
    lim.setpos(-2000,-350)
    lim.pendown()
    lim.setpos(2000,-350)
    
def scorboard():
    scor1.ht()
    scor1.speed(100)
    scor1.penup()
    scor1.goto(-180,408)
    scor1.pendown()
    scor1.clear()
    scor1.write(xp2, move = False, align ="center" , font = ("Arial",20,"normal"))
    
    scor2.ht()
    scor2.speed(100)
    scor2.penup()
    scor2.goto(180,408)
    scor2.pendown()
    scor2.clear()
    scor2.write(xp1, move = False, align ="center" , font = ("Arial",20,"normal"))
    
def scorboardtab(tab):
    tab.color("white","white")
    tab.speed(1000)
    tab.penup()
    tab.goto(-300,450)
    tab.pendown()
    tab.begin_fill()
    tab.forward(600)
    tab.setheading(270)
    tab.forward(55)
    tab.setheading(180)
    tab.forward(600)
    tab.setheading(90)
    tab.forward(55)
    tab.end_fill()
    tab.ht()

#key controls
def ply1_right():
    if ply1.ycor() < -300 and ply1.ycor() > -400:
        ply1.penup()
        ply1.setheading(0)
        ply1.forward(0)
        ply1.pendown()
    else:
        ply1.penup()
        ply1.setheading(0)
        ply1.forward(50)
        ply1.pendown()
def ply1_left():
    if ply1.ycor() < -300 and ply1.ycor() > -400:
        ply1.penup()
        ply1.setheading(0)
        ply1.backward(0)
        ply1.pendown()
    else:
        ply1.penup()
        ply1.setheading(180)
        ply1.forward(50)
        ply1.pendown()
   
def ply2_right():
    if ply2.ycor() < -300 and ply2.ycor() > -400:
        ply2.penup()
        ply2.setheading(0)
        ply2.forward(0)
        ply2.pendown()
    else:
        ply2.penup()
        ply2.setheading(0)
        ply2.forward(50)
        ply2.pendown()
  
def ply2_left():
    if ply2.ycor() < -300 and ply1.ycor() > -400:
        ply2.penup()
        ply2.setheading(0)
        ply2.backward(0)
        ply2.pendown()
    else:
        ply2.penup()
        ply2.setheading(180)
        ply2.forward(50)
        ply2.pendown()
  
def ply1_down():
    if ply1.ycor() < -300 and ply1.ycor() > -400:
        ply1.setheading(270)
        ply1.forward(0)
        ply1.setheading(0)
    else:
        ply1.penup()
        ply1.setheading(270)
        ply1.forward(630)
        ply1.setheading(0)
        ply1.pendown()
    
def ply1_up():
    if ply1.ycor() < 350 and ply1.ycor() > 250:
        ply1.setheading(90)
        ply1.forward(0)
        ply1.setheading(0)
    else:
        ply1.penup()
        ply1.setheading(90)
        ply1.forward(630)
        ply1.setheading(0)
        ply1.pendown()
    
def ply2_down():
    if ply2.ycor() < -300 and ply2.ycor() > -400:
        ply2.setheading(270)
        ply2.forward(0)
        ply2.setheading(0)
    else:
        ply2.penup()
        ply2.setheading(270)
        ply2.forward(630)
        ply2.setheading(0)
        ply2.pendown()

def ply2_up():
    if ply2.ycor() < 350 and ply2.ycor() > 250:
        ply2.setheading(90)
        ply2.forward(0)
        ply2.setheading(0)
    else:
        ply2.penup()
        ply2.setheading(90)
        ply2.forward(630)
        ply2.setheading(0)
        ply2.pendown()


can=turtle.Turtle()
canvas=turtle.Screen()

#login
canvas.screensize(4000,800,"white")
can.ht()
can.write("play fullscreen!", move = False, align ="center" , font = ("Arial",30,"normal"))
time.sleep(2)
can.clear()
can.write("\t         control keys:\n A-S-W-D(for yellow) and arrow keys(for cyan)", move = False, align ="center" , font = ("Arial",20,"normal"))
time.sleep(4)
can.clear()
can.write("\tcrash the bugs and gain xp, \nthe player who reachs 15 xp first, gonna win! ", move = False, align ="center" , font = ("Arial",20,"normal"))
time.sleep(4)
can.clear()
can.write("3!", move = False, align ="center" , font = ("Arial",70,"normal"))
time.sleep(1)
can.clear()
can.write("2!", move = False, align ="center" , font = ("Arial",70,"normal"))
time.sleep(1)
can.clear()
can.write("1!", move = False, align ="center" , font = ("Arial",70,"normal"))
time.sleep(1)
can.clear()
can.write("DEBUG!", move = False, align ="center" , font = ("Arial",100,"normal"))
time.sleep(1)
can.clear()
canvas.screensize(4000,800,"black")


#variables and turtle objects
scor=turtle.Turtle()
scor1=turtle.Turtle()
scor2=turtle.Turtle()

ply1x = 300
ply1y = 300
ply2y = 300
ply2x = -300

xp1= 0
xp2= 0

tab = turtle.Turtle()
ply1 = turtle.Turtle()
ply2 = turtle.Turtle()
limit = turtle.Turtle()
dot = turtle.Turtle()

#start of game
sınır(limit,"purple")   
rock("cyan",ply1x,ply1y,ply1)
rock("yellow",ply2x,ply2y,ply2)
scorboardtab(tab)
scor.penup()
scor.goto(0,408)
scor.pendown()
scor.write("YELLOW vs CYAN", move = False, align ="center" , font = ("Arial",20,"normal"))
scor.ht()

#for inputs from key
turtle.listen() 

turtle.onkey(ply1_right, "Right")
turtle.onkey(ply1_left, "Left")
turtle.onkey(ply1_down, "Down")
turtle.onkey(ply1_up, 'Up')

turtle.onkey(ply2_right, 'd')
turtle.onkey(ply2_left, 'a')
turtle.onkey(ply2_down, 's')
turtle.onkey(ply2_up, 'w')



while(1):
    random_bug(1,dot)
    
    #for finish game
    if xp1==15: 
        canvas.screensize(4000,800,"white")
        can.goto(0,-20)
        can.write("CYAN WIN!", move = False, align ="center" , font = ("Arial",120,"normal"))
        time.sleep(3)
        can.clear()
        exit(1)
    if xp2==15:
        canvas.screensize(4000,800,"white")
        can.goto(0,-20)
        can.write("YELLOW WIN!", move = False, align ="center" , font = ("Arial",120,"normal"))
        time.sleep(3)
        can.clear()
        exit(1)



turtle.mainloop()
   

turtle.done()