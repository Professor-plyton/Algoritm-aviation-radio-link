# Моделирование динамики изменения параметров мобильного канала
# связи методом пространства переменных состояний (State Space)
# на  примере  ДКМВ (КВ, ВЧ) канала системы  HFDL
import math
import random
import numpy as np


a = 10*2*math.pi  # ширина спектра частотных флуктуаций, рад\сек за сек (скорость изменения частоты до 10 Гц/с)
B = 10*2*math.pi  # скорость быстрых замираний, рад\сек

T0 = 1/1800 # длительность символа (элементарной посылки)  при символьной скорости 1800 Бод (симв/с)
k0 = 50 # число выборок сигнала на длительности символа
N = 50 # число символов  в сообщении
k = list(range(1, k0*N))
Ts = T0*N # длительность сообщения
T = T0 * k0**-1 # период дискретизации
p0 = 1.577 * 10**-6  # дисперсия допплеровского сдвига частоты (квадрат стандартного максимального отклонения частоты 200 Гц *2*), (рад\сек)(рад\сек),
p1 = 1 # дисперсия флуктуаций коэффициентов отражения ионосферы
p3 = (100*2*math.pi)**2 # дисперсия скорости изменения допплеровского сдвига частоты, (рад\сек)(рад\сек), для максимального стандартного отклонения 100 Гц\с
mc = 0  # математические ожидания квадратурных компонент коэффициента отражения ионосферы,
ms = 0
A = 4   # амплитуда
w0 = 2*math.pi*1440  # угловая частота сигнала  в  рад/сек
M = 2  # число градаций  сдвигов фазы

def ak(k, k0):
    ak = []
    a = []
    for x in k:
        b = x % (2*k0)
        a.append(b)
    for x in a:
        if x <= k0:
            ak.append(1)
        else:
            ak.append(0)
    return ak

def bk(ak):
    bk = [] # ортогональная кодовая последовательность
    for xbk in ak:
        xbk = 1 - xbk
        bk.append(xbk)
    return bk


def s1k(ak, w0, T, k, A, M):
    e = []
    r = []
    s1k = []
    for x in ak:
        a = (x*math.pi*2)/M
        e.append(a)
    for y in k:
        b = w0 * T * y
        r.append(b)
    t = list(map(lambda x, y: x + y, e, r))
    for i in t:
        c = pow(2, 0.5)*A* math.sin(i)
        s1k.append(c)
    return s1k

def s2k(ak, w0, T, k, A):
    e = []
    r = []
    s2k = []
    for x in ak:
        a = pow(-1, x)
        e.append(a)
    for y in k:
        b =math.sin(w0*T*y)
        r.append(b)
    t = list(map(lambda x,y: x * y, e, r))
    for i in t:
        c = i*pow(2, 0.5)*A
        s2k.append(c)
    return s2k # рабочий вариаааант



