funcs= ['Сложение', "Вычитание","Умножение","Деление","Возведение в степень","Логарифм", \
        "округление в большую сторону до N знаков после запятой", \
        "округление в меньшую сторону до N знаков после запятой"]
m="Введите необходимую функцию: Сложение, Вычитание, Умножение, Деление, Возведение в степень, \
Логарифм, \nокругление в большую сторону до N знаков после запятой, \
округление в меньшую сторону до N знаков после запятой"
print(m)
f, b1, b2 = input(), 0, 0


def sh1(b1):
    if not (b1.isdigit() or type(b1)==float):
        print('Введенный элемент не является числом, введите первый элемент:')
        b1=input()
        return sh1(b1)
    else:
        print('Введите второй элемент:')
        return float(b1)
    print()


def sh2(b2):
    b2=input()
    if not (b2.isdigit() or type(b2)==float):
        print('Введенный элемент не является числом, введите второй элемент:')
        b2=input()
        return sh2(b2)
    else:
        return float(b2)

import math

def chek(f,b1,b2):
    if str(f) not in funcs:
        print('такой функции не существует', m)
        f=input()
        return check(f,b1,b2)
    else:
        print('введите первый элемент:')
        b1=input()
        a,n=sh1(b1), sh2(b2)
        if f==funcs[0]:
            return a+n
        elif f==funcs[1]:
            return a-n
        elif f==funcs[2]:
            return a*n
        elif f==funcs[3]:
            return a/n
        elif f==funcs[4]:
            return a**n
        elif f==funcs[5]:
            return math.log(a,n)
print(chek(f,b1,b2))





