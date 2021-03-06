from kulka import Kulka
import time
from random import randint


class Codesphere(object):

    def __init__(self, address):
        self._addr = address
        self._kulka = Kulka(address)

        for _ in range(5):
            self.change_ball_color(randint(0, 255), randint(0, 255), randint(0, 255))
            time.sleep(0.1)


    def __enter__(self):
        return self


    def __exit__(self, type_, value, traceback):
        self._kulka.close()


    def set_inactivity_timeout(self, timeout):
        return self._kulka.set_inactivity_timeout(timeout)


    def change_ball_color(self, red, green, blue):
        return self._kulka.set_rgb(red, green, blue)


    def change_tail_brightness(self, bright):
        return self._kulka.set_back_led(bright)


    def set_heading(self, heading):
        return self._kulka.set_heading(heading)

    def roll(self, heading, wait):
        self._kulka.roll(175, heading, 1)
        time.sleep(wait + 0.5)
        return


    def roll_for_one_second(self, heading):
        self._kulka.roll(175, heading, 1)
        time.sleep(1 + 0.5)
        return

    def stop(self):
        self._kulka.roll(0, 0, 1)
        time.sleep(0.5)
        return

    def sleep(self, wakeup=0, macro=0, orb_basic=0):
        return self._kulka.sleep(wakeup, macro, orb_basic)
