from kulka import Kulka
import time


def main():
    print("Codesphere started!")
    with open('mysphero.txt') as file_:
       addr = file_.readline().strip()

    with Kulka(addr) as sphero:
        sphero.set_inactivity_timeout(3600)

        for _ in range(10):
            sphero.set_rgb(0xFF, 0, 0)
            time.sleep(0.1)
            sphero.set_rgb(0, 0, 0)
            time.sleep(0.1)

        sphero.sleep()

if __name__ == '__main__':
    main()
