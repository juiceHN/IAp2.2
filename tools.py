import random
import numpy as np
import matplotlib.pyplot as plt

'''
	creates random coords, 
	used to generate data for testing other functions

	number: amount of coords desired
	a, b: ranges, must be a > b

	return:
		arrayx = x only coords
		arrayy = y only coords
		other = xy coords
'''


def nCoords(number, a, b):
    arrayx = []
    arrayy = []
    other = []
    for i in range(number):
        x = random.randint(a, b)
        y = random.randint(a, b)
        c = [x, y]
        arrayx.append(x)
        arrayy.append(y)
        other.append(c)
    return arrayx, arrayy, other


def file_len(filename):
    with open(filename) as doc:
        for i, l in enumerate(doc):
            pass
    return i + 1


def cleanLine(line):
    char = "[]\n"
    for c in char:
        line = line.replace(c, "")
    line = line.lower()
    return line


def openCoords(filename):
    x, y, xy = [], [], []
    a = file_len(filename)
    doc = open(filename, 'r')
    for i in range(a):
        line = doc.readline()
        line = cleanLine(line)
        coord = line.split(',')
        xx = float(coord[0])
        yy = float(coord[1])
        x.append(xx)
        y.append(yy)
        xxyy = [xx, yy]
        c = np.array(xxyy)
        xy.append(c)
    return x, y, xy


def graphPoints(arrayx, arrayy):
    plt.scatter(arrayx, arrayy)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def maxmins(x, y):
    a = max(x)
    b = min(x)
    c = max(y)
    d = min(y)
    v = [a, b, c, d]
    return v
