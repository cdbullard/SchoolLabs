from drone import Drone


if __name__ == '__main__':
    possible_options = {0, 1, 2, 3, 4}
    rq21 = Drone()
    while True:
        try:
            innie = int(input("Enter 1 for accelerate, 2 for decelerate, 3 for ascend, 4 for descend, 0 for exit: "))
            if innie == 0:
                print("Drone Speed:", rq21.speed, "Drone Altitude:", rq21.height)
                break
            elif innie == 1:
                rq21.accelerate()
            elif innie == 2:
                rq21.decelerate()
            elif innie == 3:
                rq21.ascend()
            elif innie == 4:
                rq21.descend()
            else:
                raise ValueError
            print("Drone Speed:", rq21.speed, "Drone Altitude:", rq21.height)
        except ValueError:
            print("Please enter one of the follow integers:", possible_options)
            continue
