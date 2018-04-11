from tools import *
from calc import *

filename = 'test.txt'
num = int(input('ingrese el numero de gausianos a ajustar: '))
x,y,xy=openCoords(filename)
mmArr = maxmins(x,y)
sigma, mu, pi = genCluster(num, mmArr)

