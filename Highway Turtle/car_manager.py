from turtle import Turtle,Screen
import random



speed = 10





class CarManager():
    def __init__(self):
        self.all_cars =[]
        self.creating_car






    def creating_car(self,color):
        random_chance = random.randint(0,4)
        if random_chance ==1:
            self.car = Turtle()
            self.car.color(color)
            self.car.shape("square")
            self.car.shapesize(stretch_wid=1, stretch_len=2)
            self.car.penup()
            y = random.randint(-150,180)
            if y%30 < 15:
                new_y = y - y%30
                self.car.goto(400, new_y)
            if y%30 >= 15:
                new_y = y + (30-y%30)
                self.car.goto(400,new_y)
            self.all_cars.append(self.car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(speed)







