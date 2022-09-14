from First_two_graphs import *

# матрица вероятностей переходов
# расширенного вектора состояния или системная матрица модели переменных состояния канала
matrixF = [[1, T, 0, 0 ],
           [0,1-a*T, 0, 0],
           [0,0,1-B*T, 0],
           [0,0,0, 1-B*T]]
# матрица "вход-состояние"  или шумовая матрица
matrixG = [[0,0,0,0],[0, pow(2*a*T*p0, 0.5), 0, 0 ],[0,0, pow(2*B*T*p1,0.5),0],[0,0,0,pow(2*B*T*p1,0.5)]]

# Генерация порождающих шумов модели переменных состояний канала

# порождающий шум квадратур модели
# импульсной характеристики канала
#I3k = pow(-2*math.log(random.random()),0.5)
#w3k = I3k*math.sin(random.uniform(0, 2*math.pi))  # используем псевдослучайное вещественное число
#I4K = pow(-2*math.log(random.random()),0.5)
#w4k = I4K*math.cos(random.uniform(0, 2*math.pi))

Dw3 = 0.958
Dw4 = 0.993
Mw3 = -2.138*pow(10, -3)
Mw4 = 0.023

I2k = pow(-2*math.log(random.random()),0.5)
w2k = I2k*math.sin(random.uniform(0, 2*math.pi))
Dw2 = 0.958
Mw2 = 3.915 * pow(10, -3)

def x2k(p0,T,a, w2k):
    x2k=[]
    x20 = 2*math.pi
    x2k.append(x20)
    while len(x2k) < 2499:
        i = x2k[-1]
        b = i*(1-a*T) + (pow(2*a*T*p0,0.5)*w2k)
        x2k.append(b)
    return x2k

def x1k(x2k, T):
    x1k = []
    x10 = math.pi/2
    x1k.append(x10)
    while len(x1k) < 2499:
        for j in x2k:
            i = x1k[-1]
            b = i+j*T
            x1k.append(b)
    x1k.pop()
    return x1k

def x3k(B, T, p1):
    x3k = []
    x30 = 1
    x3k.append(x30)
    while len(x3k) < 2499:
        I3k = pow(-2 * math.log(random.random()), 0.5)
        b = math.sin(random.uniform(0, 2 * math.pi))
        w3k = I3k * b

        i = x3k[-1]
        x3k1 = (1 - B * T) * i + (pow(2 * B * T * p1, 0.5) * w3k)

        #if abs(x3k[-1] - x3k1) < random.uniform(0, 0.04):
        x3k.append(x3k1)
    return x3k

def x4k(B, T, p1):
    x4k = []
    x40 = 1
    x4k.append(x40)
    while len(x4k) < 2499:
        I4k = pow(-2 * math.log(random.random()), 0.5)
        b = math.cos(random.uniform(0, 2 * math.pi))
        w4k = I4k * b

        i = x4k[-1]
        x4k1 = (1 - B * T) * i + (pow(2 * B * T * p1, 0.5) * w4k)

       # if abs(x4k[-1] - x4k1) < random.uniform(0, 0.04):
        x4k.append(x4k1)
    return x4k

def S1K(A, w0, k, T, ak, x3k, x1k, x4k):
    a = []
    for x in k:
        a1 = x*T*w0
        a.append(a1)
    sin = list(map(lambda x, y: math.sin(x + y), a, x1k))
    cos = list(map(lambda x, y: math.cos(x + y), a, x1k))
    el1 = list(map(lambda x, y: x * y, x3k, sin))
    el2 = list(map(lambda x, y: x * y, x4k, cos))
    el3 = list(map(lambda x, y: x - y, el1, el2))

    b = []
    for i in ak:
        b1 = pow(-1, i) * pow(2,0.5) * A
        b.append(b1)
    S1K = list(map(lambda x, y: x * y, b, el3))
    return S1K

#Вычисление комплексного шума наблюдения,модели квадратур
#которого имеют релеевский закон замираний, а фазы модулей
#РАСПРЕДЕЛЕНЫ равномерно от 0 до 2п

#Вычисление синусной квадратуры шума наблюдения

Isk = pow(-2*math.log(random.random()),0.5)
esk = I2k*math.sin(random.uniform(0, 2*math.pi))

#Вычисление косинусной квадратуры шума наблюдения
Ick = pow(-2*math.log(random.random()),0.5)
eck = I2k*math.cos(random.uniform(0, 2*math.pi))

ek = esk + eck
S1K1 = S1K(A=A, w0=w0, k=k, T=T, ak=ak(k=k, k0=k0), x3k=x3k(B=B,T=T,p1=p1), x1k=x1k(x2k=x2k(p0=p0, T=T, a=a,w2k=w2k), T=T), x4k=x4k(B=B,T=T,p1=p1))

#уровнение наблюдения на входе приемника

def zk1():
    zk1 = []
    while len(zk1) < 2499:

        #Вычисление синусной квадратуры шума наблюдения

        Isk = pow(-2 * math.log(random.random()), 0.5)
        esk = Isk * math.sin(random.uniform(0, 2 * math.pi))

        # Вычисление косинусной квадратуры шума наблюдения

        Ick = pow(-2 * math.log(random.random()), 0.5)
        eck = Ick * math.cos(random.uniform(0, 2 * math.pi))
        ek = esk + eck
        zk1.append(ek)
    return zk1

zk = list(map(lambda x, y: x + y, zk1(), S1K1))