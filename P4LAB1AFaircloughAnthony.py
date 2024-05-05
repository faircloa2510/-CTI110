# Python program to draw square and a triangle 
# Using Turtle Programming
# Anthony Fairclough
# 5/3/2024

#calll up turtle program
import turtle  

win = turtle.Screen()

dog = turtle.Turtle()

#use turle to create a square

for i in range(4):
    dog.forward(100)
    dog.left(90)

dog.penup()
dog.forward(120)
dog.pendown()

#use urtle to raw a trianle

for _ in range(3):
    dog.forward(100)
    dog.left(120)

