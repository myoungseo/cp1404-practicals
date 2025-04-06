import random
from prac_09.car import Car

class UnreliableCar(Car):
    """A Car that may not always drive based on reliability."""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if a random number is less than reliability."""
        random_chance = random.uniform(0, 100)
        if random_chance < self.reliability:
            return super().drive(distance)
        else:
            return 0