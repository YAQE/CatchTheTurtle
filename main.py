import turtle
from random import randint
from turtle import *



score = 0
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("welcome to the screen")
screen.setup(width=600, height=600)
karakter = turtle.Turtle()
karakter.shape("turtle")
karakter.penup()
karakter.color("green")

scoreDisplay = turtle.Turtle()
scoreDisplay.speed(0)
scoreDisplay.color("white")
scoreDisplay.penup()
scoreDisplay.hideturtle()
scoreDisplay.goto(x=-220, y=260)




def oyun(x, y):
    karakter.hideturtle()
    karakter.goto(randint(-200, 0), randint(0, 200))
    karakter.showturtle()
    scoreBoard()



def scoreBoard():
    scoreDisplay.clear()
    global score
    score += 1
    scoreDisplay.write(f"Score: {score}" , align="center", font=("Courier", 24, "normal"))





karakter.onclick(fun=oyun, btn=1)













turtle.done()