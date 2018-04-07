import random


def nCoords(number, a, b):
    array = []
    for i in range(number):
        x = random.randint(a, b)
        y = random.randint(a, b)
        c = (x, y)
        array.append(c)
    return c


def nClusters(number):
    array = []
    a = 1
    for i in range(number):
        c = array.append(random.randint(a, 99))
        array.append(c)
        a = 100 - a
        print(a)
    print(array)


nClusters(3)
