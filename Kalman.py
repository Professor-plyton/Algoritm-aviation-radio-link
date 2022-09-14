from First_two_graphs import *
from Second_four_graphs import *

x10p =[]
x100 = math.pi / 2
x10p.append(x100)


x20p = []
x200 = math.pi * 2
x20p.append(x200)


x30p = []
x300 = 1
x30p.append(x300)


x40p = []
x400 = 1
x40p.append(x400)


V1k = []
v0 = 0
V1k.append(v0)

i = 1 # оно тута

S0K =[]
zkk = []
Hk = []
dS0k = []

Dw2 = 0.958
Dw3 = 0.958
Dw4 = 0.993

matrixF = [[1, T, 0, 0],
           [0, 1 - a * T, 0, 0],
           [0, 0, 1 - B * T, 0],
           [0, 0, 0, 1 - B * T]]

matrixG = [[0, 0, 0, 0],
           [0, pow(2 * a * T * p0, 0.5), 0, 0],
           [0, 0, pow(2 * B * T * p1, 0.5), 0],
           [0, 0, 0, pow(2 * B * T * p1, 0.5)]]

matrixVw = [[0, 0, 0, 0],
            [0, Dw2, 0, 0],
            [0, 0, Dw3, 0],
            [0, 0, 0, Dw4]]

for x in S1K1:
    # ИКС 2
    x20pl = x20p[-1]
    x20p1 = (1 - a * T) * x20pl

    # ИКС 1
    x10pl = x10p[-1]
    x10p1 = x10pl + x20pl * T

    # ИКС 3

    x30pl = x30p[-1]
    x30p1 = (1 - B * T) * x30pl

    # ИКС 4
    x40pl = x40p[-1]
    x40p1 = (1 - B * T) * x40pl

    V1kl = V1k[-1]

    akk = None
    ak1k = i % (2 * k0)
    if ak1k <= k0:
        akk = 1
    else:
        akk = 0

    S0K1 = pow(-1, akk) * pow(2, 0.5) * A * (x30p1 * math.sin
    (w0 * i * T + x10p1) - x40p1 * math.cos
    (w0 * i * T + x10p1))

    S0K.append(S0K1)

    # вычесление zk
    Isk = pow(-2 * math.log(random.random()), 0.5)
    esk = Isk * math.sin(random.uniform(0, 2 * math.pi))
    Ick = pow(-2 * math.log(random.random()), 0.5)
    eck = Ick * math.cos(random.uniform(0, 2 * math.pi))
    zk1k = esk + eck
    zkk.append(zk1k)
    Hk1 = zk1k - x
    Hk.append(Hk1)

    R = [[x30p1*math.cos(w0*i*T+x10p1) + x40p1*math.sin(w0*i*T+x10p1)],
                                    [0],
                                    [math.sin(w0*i*T+x10p1)],
                                    [-math.cos(w0*i*T+x10p1)]]
    dS0k1 = pow(-1,akk)*pow(2,0.5)*A*np.matrix(R) #был массив а не матрица
    dS0k.append(dS0k1)




    V1k11 = np.array(matrixF)*V1kl*(np.array(matrixF)**T) # был массив а не матрица  и добав 2 матрицу
    V1k12 = np.array(matrixG) * np.array(matrixVw) * (np.array(matrixG)**T)
    V1k13 = np.array(V1k11) + np.array(V1k12)
    V1k.append(V1k13)
    DE = 1.958

    Vk1 = np.array(V1k13)* np.array(dS0k1)
    Vk2 = np.array(V1k13)* (np.array(np.sign(dS0k1))*(abs(np.array(dS0k1))**T))
    Vk22 = np.array(Vk1) * np.array(Vk2)

    Vk = np.array(V1k13) - (np.array(Vk1) * np.array(Vk2))


    Kk = np.dot(Vk,dS0k1)*(DE ** -1)

    Kkalmana = Kk*Hk1

    otvet = [[x10p1],
            [x20p1],
            [x30p1],
            [x40p1]]


    otvet1 = np.array(otvet)+np.array(Kkalmana)


    x10p.extend(otvet1[0])
    x20p.extend(otvet1[1])
    """if abs(x30pl - otvet1[2]) < random.uniform(0, 0.5) and abs(x30pl - otvet1[3]) < random.uniform(0, 0.5):
        x10p.extend(otvet1[0])
        x20p.extend(otvet1[1])
        x30p.extend(otvet1[2])
        x40p.extend(otvet1[3])
        """
    x30p.extend(otvet1[2])
    x40p.extend(otvet1[3])
    i = i + 1
    if len(x40p) == 2499:
        break

