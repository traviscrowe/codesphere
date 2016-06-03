from kulka import Kulka
import time


class Codesphere(object):

    def __init__(self, address):
        self._addr = address
        self._kulka = Kulka(address)


    def __enter__(self):
        return self


    def __exit__(self, type_, value, traceback):
        self._kulka.close()


    def set_inactivity_timeout(self, timeout):
        return self._kulka.set_inactivity_timeout(timeout)


    def change_ball_color(self, red, green, blue):
        return self._kulka.set_rgb(red, green, blue)


    def chanage_tail_color(self, bright):
        return self._kulka.set_back_led(bright)


    def roll(self, heading, wait):
        self._kulka.roll(100, heading, 1)
        time.sleep(wait)
        return


    def sleep(self, wakeup=0, macro=0, orb_basic=0):
        return self._kulka.sleep(wakeup, macro, orb_basic)
