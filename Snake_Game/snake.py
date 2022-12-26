import turtle

screen = turtle.Screen()
starting_point =[(0,0),(-20,0),(-40,0)]
move_distance = 20
screen.colormode(255)

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.segments[0].color("pink")


    def create_snake(self):

        for position in starting_point:
            snake = turtle.Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.segments.append(snake)

    def add_segment(self,color_is):
        snake = turtle.Turtle("square")
        snake.color(color_is)
        snake.penup()
        snake.goto(self.segments[-1].position())
        self.segments.append(snake)

    def turn_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def turn_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def turn_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def turn_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def move(self):
        for seg in range(len(self.segments) -1, 0, -1):
            x_cor = self.segments[seg -1].xcor()
            y_cor = self.segments[seg -1].ycor()
            self.segments[seg].goto(x_cor ,y_cor)

        self.segments[0].forward(move_distance)


    def reset(self):
        for seg in self.segments:
            seg.goto(800,800)
        self.segments.clear()
        self.create_snake()
        self.segments[0].color("pink")
