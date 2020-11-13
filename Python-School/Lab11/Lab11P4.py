# started this thinking I was going to use class functions to do something different than it ended up
class HotdogStand:
    def __init__(self):
        self.hotdog_price = 2.5
        self.chip_price = 1.5
        self.soda_price = 1.25
        self.hotdog_num = 0
        self.chips_num = 0
        self.sodas_num = 0
        self.total_price = 0

    def hotdogs(self):
        my_hotdog = True
        while my_hotdog is True:
            try:
                self.hotdog_num = int(input("How many hotdogs? "))
                if self.hotdog_num < 0:
                    raise ValueError
                my_hotdog = False
            except ValueError:
                print("Invalid input")
                continue
        return self.hotdog_num

    def chips(self):
        my_chips = True
        while my_chips is True:
            try:
                self.chips_num = int(input("How many bags of chips? "))
                if self.chips_num < 0:
                    raise ValueError
                my_chips = False
            except ValueError:
                print("Invalid input")
                continue
        return self.chips_num

    def sodas(self):
        my_sodas = True
        while my_sodas is True:
            try:
                self.sodas_num = int(input("How many sodas? "))
                if self.sodas_num < 0:
                    raise ValueError
                my_sodas = False
            except ValueError:
                print("Invalid input")
                continue
        return self.sodas_num

    def total(self):
        self.total_price = self.chips_num * self.chip_price + self.hotdog_num * self.hotdog_price + self.sodas_num * \
                           self.soda_price
        return self.total_price


if __name__ == '__main__':
    my_hotdog_stand = HotdogStand()
    my_hotdog_stand.hotdogs()
    my_hotdog_stand.chips()
    my_hotdog_stand.sodas()
    my_hotdog_stand.total()
    print(f"Please pay this amount: ${my_hotdog_stand.total_price:.2f}")
