def t1():
    x = int(input("Enter X: "))
    y = int(input("Enter Y: "))

    if x > 8:
        z = 3 + y
    else:
        z = 9 * x * y
    print("Z = ", z)


def t2():
    n = int(input("Enter N: "))
    z = int(1)
    for i in range(n):
        z = z * (i + 1)
    print("Z = ", z)


f = int(0)
while f != 3:
    print("1. Решить пример \n2. Найти факториал \n3. Выход")
    f = int(input())

    if f == 1:
        t1()

    elif f == 2:
        t2()

    elif f == 3:
        break
