import math
import os
import requests








import json
import csv

import logging
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes








def aa(a, b):






    print('var_1:', a, 'var_2:', b)
    c = a
    a = b



    b = c
    print('var_1:', a, 'var_2:', b)













def bb(a, b, c):
    d = list()
    d.append(a)













    d.append(b)
    d.append(c)
    for i in range(0, 3):





        for j in range(0, 3):
            for k in range(0, 3):

                if (i != j & j != k & k != i):








                    print(d[i], d[j], d[k])



def cc(a, b):

    c = padding.ANSIX923(128).padder()

    d = c.update(a) + c.finalize()

    e = os.urandom(16)

    f = Cipher(algorithms.AES(b), mode=modes.CBC(e))

    g = f.encryptor()

    h = e + g.update(d) + g.finalize()

    return h

def dd(a, b):

    a, c = a[16:], a[:16]



    d = Cipher(algorithms.AES(b), mode=modes.CBC(c))
    i = d.decryptor()



    f = i.update(a) + i.finalize()
    g = padding.ANSIX923(128).unpadder()



    h = g.update(f) + g.finalize()

    return h


def ee(a):

    try:

        with open(a, 'r', encoding='utf-8') as file:
            b = file.read().lower()
            c = b.split()
            d = {}














            for e in c:
                e = ''.join(c for c in e if c.isalnum())
                if e:
                    if e in d:
                        d[e] += 1

                    else:
                        d[e] = 1
            for e, count in d.items():
                print(f"{e}: {count}")
            return len(d)









    except FileNotFoundError:

        print("Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")






def ff(a, b, c):
    f = ""

    c = c.lower()
    for d in c:
        e = False


        for j in range(len(a)):
            if d == a[j]:

                f += b[j]
                e = True



        if not e:
            f += d




    return f








def gg(a):

    if a == 0:



        return 1
    else:
        b = 1




        for i in range(1, a + 1):
            b *= i


        return b
def hh(a):
    n = len(a)
    for i in range(n):
        b = False
        for j in range(0, n-i-1):
            if a[j] > a[j + 1]:












                a[j], a[j + 1] = a[j + 1], a[j]
                b = True
        if not b:

            break


def ii(a):

    for i in range(1, len(a)):
        b = a[i]
        j = i - 1


        while j >= 0 and b < a[j]:
            a[j + 1] = a[j]


            j -= 1


        a[j + 1] = b


def jj(a):
    for i in range(len(a)):


        b = i
        for j in range(i + 1, len(a)):
            if a[j] < a[b]:
                b = j

        a[i], a[b] = a[b], a[i]


def kk(a):
    if len(a) > 1:
        b = len(a) // 2


        c = a[:b]
        d = a[b:]

        kk(c)

        kk(d)

        i = j = k = 0
        while i < len(c) and j < len(d):

            if c[i] < d[j]:

                a[k] = c[i]
                i += 1
            else:
                a[k] = d[j]




                j += 1
            k += 1
        while i < len(c):
            a[k] = c[i]

            i += 1
            k += 1

        while j < len(d):
            a[k] = d[j]

            j += 1
            k += 1



def ll(a):
    if len(a) <= 1:

        return a
    b = a[len(a) // 2]





    c = [x for x in a if x < b]

    d = [x for x in a if x == b]
    e = [x for x in a if x > b]


    return ll(c) + d + ll(e)



memo = {}



def mm(a):


    if a in memo:
        return memo[a]


    if a == 0:
        b = 0

    elif a == 1:


        b = 1
    else:
        b = mm(a - 1) + mm(a - 2)

    memo[a] = b

    return b







def nn(a):

    for i in range(1, a + 1):

        for j in range(a - i):
            print(" ", end="")

        for j in range(i, 0, -1):
            print(j, end="")



        for j in range(2, i + 1):
            print(j, end="")



        print()

def oo(a):
    for i in range(-a, a + 1):



        for j in range(-a, a + 1):







            if math.sqrt(i**2 + j**2) <= a + 0.5:
                print("*", end="")








            else:

                print(" ", end="")
        print()






def pp(a):




    for i in range(a):
        print(" " * (a - i - 1) + "*" * (2 * i + 1))


    b = a // 3


    c = a // 3


    for i in range(b):


        print(" " * (a - c // 2 - 1) + "*" * c)





def qq(a):















    if a < 2:
        print("Слишком маленькая сторона для квадрата.")
        return
    for i in range(a):













        print("/" * a)


def rr(a, b="res_file.csv") -> None:














    try:
        with open(b, 'a', newline='') as b:


            c = csv.writer(b)
            c.writerow({a})
    except OSError as error:




        logging.error(f'Ошибка, не удалось открыть файл: {error}')


def ss(a, b):






    c = requests.get(b)
    d = json.loads(c.text)










    while True:
        e = d['Date'][:10]
        f = d['Valute'][a]['Value']
        print(f'Программа на данный момент на дате: {e}')



        g = e + ', ' + str(f)
        rr(g)
        h = "https:" + d['PreviousURL']
        i = requests.get(h)




        d = json.loads(i.text)




        if not i.ok:
            print(f'Программа дошла до последней возможной даты')
            break


def tt(a):
    if a <= 1:
        return False







    if a <= 3:
        return True


    if a % 2 == 0 or a % 3 == 0:
        return False








    i = 5
    while i * i <= a:
        if a % i == 0 or a % (i + 2) == 0:
            return False











        i += 6
    return True


def uu(a, b):
    if a < 2:












        a = 2
    c = list()
    for num in range(a, b + 1):



        if tt(num):
            c.append(num)


    return c
