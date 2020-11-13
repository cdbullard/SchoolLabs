from random import randint


class Lottery:
    def __init__(self):
        self.range = range(1, 11)
        self.numbers = []
        self.count = 4

    def user_picks(self):
        while self.count > 0:
            pick = int(input("Enter a number: "))
            while pick not in self.range:
                pick = int(input("Must choose a number between 1 and 10: "))
            while pick in self.numbers:
                pick = int(input("Cannot choose the same number twice, choose again: "))
            self.numbers.append(pick)
            self.count = self.count - 1
        return self.numbers.sort()

    def lottery_picks(self):
        while self.count > 0:
            pick = randint(1, 10)
            while pick in self.numbers:
                pick = randint(1, 10)
            self.numbers.append(pick)
            self.count = self.count - 1
        return self.numbers.sort()


if __name__ == '__main__':
    user = Lottery()
    user.user_picks()
    lotto = Lottery()
    lotto.lottery_picks()
    print("Numbers picked: {}".format(user.numbers))
    print("Balls drawn: {}".format(lotto.numbers))
    matches = [x for x in user.numbers if x in lotto.numbers]
    print("Number of matches: {}".format(len(matches)))
