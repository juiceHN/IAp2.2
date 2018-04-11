import random
import numpy as np


def genMat():
    inversible = True
    while inversible:
        mat = ''
        b = random.randint(-5, 5)
        c = random.randint(-5, 5)
        A1 = [0, b]
        A2 = [c, 0]
        mat = [A1, A2]
        matrix = np.array(mat)
        calc = np.linalg.det(matrix)
        if calc > 0.1 or calc < -0.1:
            inversible = False
            return matrix


def genMu(mxx, mnx, mxy, mny):
    x = random.randint(mxx, mnx)
    y = random.randint(mxy, mny)
    a = [x, y]
    a = np.array(a)
    return a


def nClusters(number):
    array = np.random.dirichlet(np.ones(number), size=1)
    return array


def genCluster(number, mmxy):
    sigma, mu = [], []
    pi = nClusters(number)
    for i in range(number):
        a = genMat()
        b = genMu(mmxy[0], mmxy[1], mmxy[2], mmxy[3])
        sigma.append(a)
        mu.append(b)
    return sigma, mu, pi


def nnp(Kpi, sigma, coord, mu):
    a = Kpi * ((2 * np.pi)**(-1))
    b = (abs(np.linalg.det(sigma))**(-0.5))
    c = (coord - mu)
    d = np.transpose(c) @ np.linalg.inv(sigma) @ c
    res = a * b * np.exp(-0.5 * d)
    print('nnp res: ', res)
    return res


def newPiCalc(coordLenght, eArray):
    x = sum(eArray) / coordLenght
    return x


def newMuCalc(coordsArray, eArray):
    a = sum(eArray)
    b = 0
    for i in range(len(coordsArray)):
        b = b + (coordsArray[i] * eArray[i])
    return b / a


def newSigmaCalc(coordsArray, eArray, mu):
    a = sum(eArray)
    b = 0
    for i in range(len(coordsArray)):
        b = b + (eArray[i] * (np.array([coordsArray[i] - mu])) * (np.transpose([coordsArray[i] - mu])))
    return b / a


def expMax(coordsArray, piArray, muArray, sigmaArray):
    newPiArray, newMuArray, newSigmaArray = [], [], []
    e_norm = []
    for j in range(len(coordsArray)):
        R = 0.0
        for i in range(len(piArray)):
            e_ij = nnp(piArray[i], sigmaArray[i], coordsArray[j], muArray[i])
            # print('e_ij', e_ij)
            R += e_ij
            # print('R: ',R)
        for k in range(len(piArray)):
            e_ij = nnp(piArray[i], sigmaArray[i], coordsArray[j], muArray[i])
            print('@e_ij: ',e_ij)
            norm = e_ij / R
            e_norm.append(norm)
    for l in range(len(piArray)):
        print('&&&update&&&')
        print(len(coordsArray))
        print(e_norm)
        newPi = newPiCalc(len(coordsArray), e_norm[l])
        newPiArray.append(newPi)
        print("$$$$$$$new Pi: ", newPi)
        newMu = newMuCalc(coordsArray, e_norm[l])
        newMuArray.append(newMu)
        newSigma = newSigmaCalc(coordsArray, e_norm[l], muArray[l])
        newSigmaArray.append(newSigma)

    return newPiArray, newSigmaArray, newMuArray


def compareArray(arr1, arr2):
    a = []
    b = 0
    for i in range(len(arr1)):
        b = abs(arr1[i] - arr2[i])
        a.append(b)
    for j in a:
        if j.all() > 1e-4:
            b += 1
    c = (b * 100) / len(arr1)
    return c


def expMax2(coordsArray, piArray, muArray, sigmaArray):
    change = True
    print('############################')
    print('pi', piArray)
    print('mu', muArray)
    print('sigma', sigmaArray)
    print('############################')
    cont = 0
    while change:
        cont += 1
        newPi, newSigma, newMu = expMax(
            coordsArray, piArray, muArray, sigmaArray)
        for i in range(len(piArray)):
            print('############################')
            print('ok')
            print('############################')
            print('pi', newPi)
            print('mu', newSigma)
            print('sigma', newMu)
            print('############################')
        if cont > 1:
            change = False


r = [-10, 10, -20, 10]
a = genMat()
b = genMu(-10, 10, -20, 10)
print('#################', b)
c = 0.21212
xy = [[2, 3],[4,5]]
xy = np.array(xy)
print('#################', xy)

p = nnp(c, a, xy[0], b)
print('@@@@@@')
print(p)
sigma, mu, pi = genCluster(2, r)
print('**********')
print(expMax(xy, pi, mu, sigma))
'''
p = [[1, 2], [8, 3]]
sigma, mu, pi = genCluster(2, r)
p = np.array(p)

expMax2(p, pi, mu, sigma)
'''