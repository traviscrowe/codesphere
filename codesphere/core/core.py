from kulka import Kulka
import time


class Codesphere(object):

    def __init__(self, address):
        self._addr = address
        self._kulka = Kulka(address)

        for _ in range(5):
            self.change_ball_color(0xFF, 0, 0)
            time.sleep(0.1)
            self.change_ball_color(0, 0, 0)
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


    def roll(self, heading, wait):
        self._kulka.roll(100, (heading - 1), 1)
        time.sleep(wait)
        return


    def roll_for_one_second(self, heading):
        self._kulka.roll(100, (heading - 1), 1)
        time.sleep(2)
        return


    def sleep(self, wakeup=0, macro=0, orb_basic=0):
        return self._kulka.sleep(wakeup, macro, orb_basic)
