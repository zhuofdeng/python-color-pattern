import turtle
import colorgram
from turtle import Turtle, Screen, window_height
import random

turtleGraphic = Turtle()
screen = Screen()
turtle.colormode(255)

def extraRGBColors():
    rgbColors = []
    extraedColors = colorgram.extract("kirby.png", 30)
    for color in extraedColors:
        rgbColors.append((color.rgb.r, color.rgb.g, color.rgb.b))

    return rgbColors

colorPallet = extraRGBColors()

def drawDot(dotSize, dotSpacing):
    turtleGraphic.pendown()
    turtleGraphic.dot(dotSize, random.choice(colorPallet))
    turtleGraphic.penup()
    turtleGraphic.forward(dotSpacing)

def makeGrid(x_size, y_size):
    DOT_SIZE = 20
    DOT_SPACING = 50

    windowWidth = (x_size - 2) * (DOT_SIZE/2) + ((x_size - 2) * DOT_SPACING)
    windowHeight = (y_size - 2) * (DOT_SIZE/2) + ((y_size - 2) * DOT_SPACING)
    screen.setup(windowWidth, windowHeight)
    print(windowWidth)
    print(windowHeight)
    currentPositionX = -(screen.window_width()/2) + (DOT_SIZE/2)
    currentPositionY = -(screen.window_height()/2) + DOT_SIZE
    turtleGraphic.penup()
    turtleGraphic.goto(currentPositionX, currentPositionY)

    for y in range(y_size):
        for x in range(x_size):
            drawDot(DOT_SIZE, DOT_SPACING)
            currentPositionX += DOT_SPACING
        currentPositionY += DOT_SPACING
        currentPositionX = -(screen.window_width()/2) + DOT_SIZE/2
        turtleGraphic.setpos(currentPositionX, currentPositionY)
    screen.exitonclick()

makeGrid(10, 10)