from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


car_list=[]


class CarManager():
    def __init__(self):
        self.MOVE_INCREMENT = 10
        self.difficulty = 6
        self.create_car()


    def create_car(self):
        random_chance=random.randint(1, self.difficulty)
        if random_chance==1:
            car = Turtle()
            car.shape("square")
            car.shapesize(1,2)
            car.color(random.choice(COLORS))
            car.penup()
            new_y=random.randint(-250, 250)
            car.goto(x=290, y=new_y)
            car_list.append(car)
    def move(self):
        for car in car_list:
            car.backward(self.MOVE_INCREMENT)

    def getList(self):
        return car_list

    def leve_up(self):
        self.difficulty+=2
        self.MOVE_INCREMENT+=1
