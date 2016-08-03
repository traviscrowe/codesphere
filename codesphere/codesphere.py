from kulka import Kulka
from core.core import Codesphere
from random import randint
import time


def main():
    _forward = 360
    _backward = 180
    _left = 270
    _right = 90

    with open('mysphero.txt') as file_:
        addr = file_.readline().strip()

    with Codesphere(addr) as codesphere:
        codesphere.set_inactivity_timeout(3600)
        codesphere.change_tail_brightness(100)

        #   YOUR CODE HERE  #
        # roll in a random direction every 3 seconds 10 times
        #for _ in range(10):
            #codesphere.roll(randint(1, 360), 1)

        codesphere.roll_for_one_second(360)
        codesphere.roll_for_one_second(180)

        codesphere.sleep()

if __name__ == '__main__':
    main()
