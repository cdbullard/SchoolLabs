class Drone:
    def __init__(self):
        self.__speed = float(0)
        self.__height = float(0)

    def __str__(self):
        return f"Speed: {self.__speed}; Height: {self.__height}"

    def accelerate(self):
        self.__speed += 10

    def decelerate(self):
        self.__speed -= 10

    def ascend(self):
        self.__height += 10

    def descend(self):
        if self.__height >= 10:
            self.__height -= 10



