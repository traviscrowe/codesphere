from kulka import Kulka
from core.core import Codesphere
from random import randint
import time


def main():
    with open('mysphero.txt') as file_:
        addr = file_.readline().strip()

    with Codesphere(addr) as sphero:
        #   SETUP SPHERO
        sphero.set_inactivity_timeout(3600)
        sphero.change_tail_brightness(100)

        #   CHANGE THE SPHERO'S COLOR
        sphero.change_ball_color(255, 0, 125)

        #   NAVIGATE THROUGH THE MAZE
        sphero.roll(0, 0.5)



        #   END
        sphero.stop()

if __name__ == '__main__':
    main()
