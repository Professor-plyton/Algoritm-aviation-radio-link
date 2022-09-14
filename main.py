# -*- coding: utf8 -*-

from control.matlab import *
from First_two_graphs import *
from Second_four_graphs import *
from Kalman import *
import matplotlib.pyplot as plt

""""
plt.plot(k, x1k(x2k(p0=p0, T=T, a=a, w2k=w2k), T=T))
plt.plot(k, x10p)
plt.show()

plt.plot(k, x2k(p0=p0,T=T,a=a, w2k=w2k))
plt.plot(k, x20p)
plt.show()

plt.plot(k, x3k(B=B, T=T, p1=p1))
plt.plot(k, x30p)
plt.show()

plt.plot(k, x4k(B=B, T=T, p1=p1))
plt.plot(k, x40p)
plt.show()
"""

#Фильтр Калмана
plt.plot(k, x10p)
plt.plot(k, x1k(x2k(p0=p0, T=T, a=a, w2k=w2k), T=T))
plt.show()

plt.plot(k, x20p)
plt.plot(k, x2k(p0=p0,T=T,a=a, w2k=w2k))
plt.show()

plt.rcParams["figure.figsize"] = (20,3)
plt.plot(k, x30p)
#plt.plot(k, x3k(B=B, T=T, p1=p1))
plt.show()

plt.rcParams["figure.figsize"] = (20,3)
plt.plot(k, x40p)
#plt.plot(k, x4k(B=B, T=T, p1=p1))
plt.show()




# первый график - график последовательность
plt.rcParams["figure.figsize"] = (20,3)
plt.axis([0, 500, -2, 2])# задаем длинну и размерноть графика
plt.plot(k, bk(ak(k=k, k0=k0)))
plt.plot(k, ak(k=k, k0=k0))
plt.show()

#второй график представление
plt.rcParams["figure.figsize"] = (20,3)
plt.axis([0, 1000, -10, 10])  # задаем длинну и размерноть графика
plt.plot(k, s1k(ak(k=k, k0=k0), w0=w0, T=T, k=k, A=A, M=M))
plt.plot(k, s2k(ak(k=k, k0=k0), w0=w0, T=T, k=k, A=A))
plt.show()

#третий график Динамика изменения  доплеровского сдвига частоты сигналаа
plt.rcParams["figure.figsize"] = (20,3)
plt.axis([0, 3000, 0, 8])
plt.plot(k, x2k(p0=p0,T=T,a=a, w2k=w2k))
plt.show()

#четвертый график Динамика изменения  доплеровской фазы сигнала
plt.rcParams["figure.figsize"] = (20,3)
plt.plot(k, x1k(x2k(p0=p0, T=T, a=a, w2k=w2k), T=T))
plt.show()

#5 график Быстрые замирания синусовой компоненты импульсной характеристики канала
plt.title('косинус')
#plt.rcParams["figure.figsize"] = (20,3)
plt.axis([0, 2500, -3, 3])
plt.plot(k, x3k(B=B, T=T, p1=p1))
plt.show()

#6 график Быстрые замирания косинусной компоненты импульсной характеристики канала
plt.title('синус')
#plt.rcParams["figure.figsize"] = (20,3)
plt.axis([0, 2500, -3, 3])
plt.plot(k, x4k(B=B, T=T, p1=p1))
plt.show()

#7 график Моделирование комплексного  сигнала, прошедшего через ДКМВ канал
#с  допплеровским  сдвигом частоты,  фазы  и  быстрыми замираниями огибающей
plt.rcParams["figure.figsize"] = (20,3)
plt.plot(k, S1K1)
plt.show()


#8 график Вычисление графика отношения  сигнал/шум в  дБ

plt.rcParams["figure.figsize"] = (20,3)
plt.plot(k, zk)
plt.plot(k, zk1(), 'ro')
plt.show()








