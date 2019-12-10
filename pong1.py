import turtle

wn  = turtle.Screen()
wn.title("Pong by Nolyfe")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)



#score keeping
score_a = 0
score_b = 0

#add Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #max speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#add Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #max speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#add Ball
ball = turtle.Turtle()
ball.speed(0) #max speed infinite
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1     #speed of the ball
ball.dy = 0.1     #speed of the ball

# create a turtle or pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write("FoxBurrito: 0   Nolyfe: 0", align="center", font=("Courier", 24, "normal"))

#Function for paddle A
def paddle_a_up():
	y = paddle_a.ycor() #to determine where the paddle is
	y += 20 #add 20 pixels to y coord
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor() #to determine where the paddle is
	y -= 20 #add 20 pixels to y coord
	paddle_a.sety(y)

#Keyboard Binding to call function
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")


#Function for paddle B
def paddle_b_up():
	y = paddle_b.ycor() #to determine where the paddle is
	y += 20 #add 20 pixels to y coord
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor() #to determine where the paddle is
	y -= 20 #add 20 pixels to y coord
	paddle_b.sety(y)

#Keyboard Binding to call function
wn.listen()
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



#Time to get the ball to move and BOUNCE




#main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border limits
    if ball.ycor() > 290:
    	ball.sety(290)
    	ball.dy *= -1           # *= -1 this makes the ball reverse direction
    if ball.ycor() < -290:
    	ball.sety(-290)
    	ball.dy *= -1    	
    if ball.xcor() > 390:
    	ball.goto(0, 0)
    	ball.dx *= -1	
    	score_a += 1
    	pen.clear()
    	pen.write("FoxBurrito: {}   Nolyfe: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
    	ball.goto(0, 0)
    	ball.dx *= -1	
    	score_b += 1    
    	pen.clear()
    	pen.write("FoxBurrito: {}   Nolyfe: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))	

	#paddle and ball bouncing
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
    	ball.setx(340)
    	ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
    	ball.setx(-340)
    	ball.dx *= -1


