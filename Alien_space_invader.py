import turtle
import winsound
from random import randint

#setting the screen of our game
main_screen = turtle.Screen()
main_screen.bgcolor("black")
main_screen.title("Space Invaders")
main_screen.bgpic("space_invaders_background.gif")

# register the shapes
turtle.register_shape("player.gif")
turtle.register_shape("invader.gif")

#setting the border of our game
pen = turtle.Turtle()
pen.speed(0)
pen.shape("triangle")
pen.color("white")
pen.penup()
pen.setposition(-300,-300)
pen.pendown()

#setting the initial score
score = 0

# Drawing the score on Screen
score_screen = turtle.Turtle()
score_screen.speed(0)
score_screen.color("white")
score_screen.penup()
score_screen.setposition(-290,280)
scorestring = "Score : {}".format(score)
score_screen.write(scorestring)
score_screen.hideturtle()

#Drawing border using loop
for item in range(4):
    pen.fd(600)
    pen.lt(90)
pen.hideturtle()

#creating bullet
bullet = turtle.Turtle()
bullet.speed(0)
bullet.color("yellow")
bullet.shape("triangle")
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.penup()
bullet.hideturtle()
#set bullet state , ready- ready to fire , fired- bullet is fired
bulletstate = "ready"
bulletspeed = 20

#creating enemy
enemies = []
no_of_enemies = randint(3,5)
for i in range(no_of_enemies):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.speed(0)
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.setposition(randint(-200,200),randint(90,250))
enemyspeed = 2

#creating player of the game
player = turtle.Turtle()
player.penup()
player.speed(0)
player.color("green")
player.shape("player.gif")
player.setheading(90)
player.setposition(0,-245)

playerspeed = 15

# defining functions for our player's spaceship
def moveleft():
    x = player.xcor()
    x -= playerspeed
    if x<-280:
        player.setx(-280)
    else:
        player.setx(x)

def moveright():
    x = player.xcor()
    x += playerspeed
    if x>280:
        player.setx(280)
    else:
        player.setx(x)

def fire_bullet():
    # set bulletstate as global as it has to be changed inside function
    global bulletstate
    # move the bullet above the player
    if bulletstate == "ready":
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()
        bulletstate = "fired"

def is_collision(t1,t2):
    # Using distance Formula
    distance = (((t1.xcor() - t2.xcor())** 2) + ((t1.ycor() - t2.ycor())** 2))**0.5
    if distance < 19:
        return True
    else:
        return False

# Binding keys to movement functions of player's spaceship
turtle.listen()
turtle.onkey(moveleft,"Left")
turtle.onkey(moveright,"Right")
turtle.onkey(fire_bullet,"space")

# main game loop
while True:
    for enemy in enemies:
        # move the enemies
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #move the enemies back and down
        if enemy.xcor()<-280:
            for item in enemies:
                y = item.ycor()
                y -= 40
                item.sety(y)
            enemyspeed *= -1

        if enemy.xcor()> 280:
            for item in enemies:
                y = item.ycor()
                y -= 40
                item.sety(y)
            enemyspeed *= -1

        #move the bullet
        if bulletstate == "fired":
            winsound.PlaySound("laser.wav",winsound.SND_ASYNC)
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)

        if  bullet.ycor() > 275:
            bullet.hideturtle()
            bullet.sety(0)
            bulletstate = "ready"

        if is_collision(enemy,bullet):
            winsound.PlaySound("explosion.wav",winsound.SND_ASYNC)
            bullet.hideturtle()
            bullet.setposition(0,-400)
            bulletstate = "ready"
            enemy.setposition(randint(-200,200),randint(90,250))
            score_screen.clear()
            score += 10
            scorestring = "Score : {}".format(score)
            score_screen.write(scorestring)

        if is_collision(enemy,player):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

turtle.done()
