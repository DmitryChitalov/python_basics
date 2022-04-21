import time
import threading


class TrafficLight:
    def __init__(self, _colors2, _colors):
        pass

    _color = None
    _colors2 = ['red']
    _colors = ['yellow', 'green']

def running():
    c = 0
    while c < 1:
        for element in TrafficLight._colors2:
            print(element)
            c += 1
            time.sleep(7)


def running2():
    c = 0
    while c < 1:
        for element in TrafficLight._colors:
            print(element)
            c += 1
            time.sleep(2)


t1 = threading.Thread(target=running())
t2 = threading.Thread(target=running2())

t1.start()
t2.start()
