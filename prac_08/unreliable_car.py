from car import Car
from random import randint

class UnreliableCar(Car):
    reliability = 0

    def __init__(self, name, fuel, reliability):
        self.reliability = reliability
        super().__init__(name, fuel)

    def drive(self, distance):
        if randint(0, 100) < self.reliability:
            #Drive Car
            super().drive(distance)

