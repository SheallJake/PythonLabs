a = int(input("Введіть значення А: "))
while 1 > a or a > 100:
    a = int(input("Введіть значення А: "))

b = int(input("Введіть значення B: "))
while 1 > b or b > 100:
    b = int(input("Введіть значення B: "))

if a == b:
    print("X = -4")
elif a < b:
    c = float((a * 3 - 5) / b)
    print("X= ", round(c, 2))
else:
    c = float((pow(a, 4) + b) / a)
    print("X=", round(c, 2))