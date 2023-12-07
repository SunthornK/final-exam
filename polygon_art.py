import turtle
import random


class Polygon_art:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = Polygon_art.get_new_color(self)
        self.border_size = random.randint(1, 10)
        self.reduction_ratio = 0.618

    def drawing(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    def get_new_color(self):
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    def reduction(self):
        reduction_ratio = 0.618
        turtle.penup()
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]
        self.size *= reduction_ratio


class Draw_simulator:
    def __init__(self, choices):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        if choices == 1:
            draw = Polygon_art(3)
            for i in range(30):
                draw.drawing()
                draw.reduction()
        elif choices == 2:
            draw = Polygon_art(4)
            for i in range(30):
                draw.drawing()
                draw.reduction()
        elif choices == 3:
            draw = Polygon_art(5)
            for i in range(30):
                draw.drawing()
                draw.reduction()
        elif choices == 4:
            draw = Polygon_art(5)
            for i in range(30):
                draw.drawing()
                draw.reduction()
        elif choices == 5:
            draw = Polygon_art(5)
            for i in range(30):
                draw.drawing()
                draw.reduction()
        elif choices == 6:
            draw = Polygon_art(5)
            for i in range(30):
                draw.drawing()
                draw.reduction()
        elif choices == 7:
            draw = Polygon_art(5)
            for i in range(30):
                draw.drawing()
                draw.reduction()
        elif choices == 8:
            draw = Polygon_art(5)
            for i in range(30):
                draw.drawing()
                draw.reduction()


choices = int(input("Which art do you want to generate? Enter a number between 1 to 8, inclusive:"))
my_simulator = Draw_simulator(choices)
