from math import ceil, floor, sqrt
from random import uniform as randflt


if __name__ == '__main__':
    my_float = randflt(1.5, 4.5)
    print("Random number generated: {}\nOutput of floor function: {}\nOutput of ceil function: {}\nOutput of sqrt "
          "function: {}".format(my_float, floor(my_float), ceil(my_float), sqrt(my_float)))
