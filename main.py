import numpy as np


def nefun(a):
    return a+1

##Нужно будет создать класс функций, чтобы находило производную, наверное. Или создать функцию, которая возвращает производную, это удобнее, т.к. их не много.

class Neuro(object):
    def __init__(self, base, minrand=0, maxrand=1, fun=nefun):          ##Первое число в массиве "базы" нейросети - число входных переменных, последнее - выходных
        self.fun = fun
        self.vfun=np.vectorize(fun)
        self.base = base
        l = len(base)
        base = base
        a = [np.random.uniform(minrand, maxrand, (base[i], base[i+1])) for i in range(l-1)]
        self.struct = a                                         ##Массив матриц, 1 матрица - 1 слой нейронов, 1 строка в матрице - коэфф-ты нейронов следующего слоя для 1 нейрона в этом слою, т.е. его "выходные синапсы"
    def think(self, input):                 ##Обработка информации
        for i in self.struct:
            input=self.vfun(input)
            input=np.dot(input, i)
        return input
def train(N, data, speed, turbo, times=1):          #data - массив, сост. из нескольких эл-тов, каждый - пара массивов: первый - вход, второй - выход
    for sran in range(times):
        for inout in data:
            bestout=inout[1]
            input=inout[0]
            out=N.think(input)
            d=[bestout-out]


