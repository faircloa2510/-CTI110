# Python program to draw my initials 
# using Turtle Programming
# Anthony Fairclough
# 5/3/2024

#calll up turtle program

import turtle

#Create a turtle screen
screen = turtle.Screen()

#Create a turtle object
dog = turtle.Turtle()

dog.color("blue")


#Function to draw the letter A
def draw_A():
    dog.left(60)
    dog.forward(100)
    dog.right(120)
    dog.forward(100)
    dog.backward(50)
    dog.right(120)
    dog.forward(50)
    dog.penup()
    dog.backward(125)
def draw_F():
    dog.pendown()
    dog.right(90)
    dog.forward(50)
    dog.backward(90)
    dog.forward(90)
    dog.right(90)
    dog.forward(60)
    dog.backward(60) 
    dog.right(90)
    dog.forward(40)
    dog.left(90)
    dog.forward(35)
    #dog.backward(50)

# Draw the letter A
draw_A()
draw_F()
