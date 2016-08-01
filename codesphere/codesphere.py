from kulka import Kulka
from core.core import Codesphere
from random import randint
import time


def main():
    _forward = 359
    _backward = 179
    _left = 179
    _right = 89

    with open('mysphero.txt') as file_:
        addr = file_.readline().strip()

    with Codesphere(addr) as codesphere:
        codesphere.set_inactivity_timeout(3600)
        codesphere.chanage_tail_color(100)

        # blink for a few seconds
        for _ in range(10):
            codesphere.change_ball_color(0xFF, 0, 0)
            time.sleep(0.1)
            codesphere.change_ball_color(0, 0, 0)
            time.sleep(0.1)

        # roll in a random direction every 3 seconds 10 times
        for _ in range(10):
            codesphere.roll(randint(0, 359), 3)

        codesphere.chanage_tail_color(10)
        codesphere.sleep()

if __name__ == '__main__':
    main()
