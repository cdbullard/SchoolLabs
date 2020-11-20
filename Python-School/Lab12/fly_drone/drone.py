class Drone:
    def __init__(self):
        self.speed = float(0)
        self.height = float(0)

    def accelerate(self):
        self.speed += 10

    def decelerate(self):
        self.speed -= 10

    def ascend(self):
        self.height += 10

    def descend(self):
        if self.height >= 10:
            self.height -= 10


