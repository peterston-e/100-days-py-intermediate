from turtle import Turtle
import random

COLORS = ["red", "orange", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LANE_1_START = (500, -250)
LANE_2_START = (-500, -200)
LANE_3_START = (500, -150)
LANE_4_START = (-500, -100)
LANE_5_START = (500, -50)


class CarManager:

    def __init__(self):
        self.lane_1 = []
        self.lane_2 = []
        self.lane_3 = []
        self.lane_4 = []
        self.lane_5 = []
        self.speed_increase = 0

    def create_car(self, lane):
        random_chance = random.randint(1, 30)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2)
            new_car.penup()

            if lane == "lane_1":
                new_car.color(COLORS[0])
                self.lane_1.append(new_car)
                new_car.goto(LANE_1_START)
            elif lane == "lane_2":
                new_car.color(COLORS[1])
                self.lane_2.append(new_car)
                new_car.goto(LANE_2_START)
            elif lane == "lane_3":
                new_car.color(COLORS[2])
                self.lane_3.append(new_car)
                new_car.goto(LANE_3_START)
            elif lane == "lane_4":
                new_car.color(COLORS[3])
                self.lane_4.append(new_car)
                new_car.goto(LANE_4_START)
            elif lane == "lane_5":
                new_car.color(COLORS[4])
                self.lane_5.append(new_car)
                new_car.goto(LANE_5_START)

    def move_lane_1(self):
        for car in self.lane_1:
            car.backward(STARTING_MOVE_DISTANCE + self.speed_increase)

    def move_lane_2(self):
        for car in self.lane_2:
            car.forward(STARTING_MOVE_DISTANCE + self.speed_increase)

    def move_lane_3(self):
        for car in self.lane_3:
            car.backward(STARTING_MOVE_DISTANCE + self.speed_increase)

    def move_lane_4(self):
        for car in self.lane_4:
            car.forward(STARTING_MOVE_DISTANCE + self.speed_increase)


    def move_lane_5(self):
        for car in self.lane_5:
            car.backward(STARTING_MOVE_DISTANCE + self.speed_increase)

