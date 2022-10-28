from random import randint
a = []
b = 0
for i in range(10):
    a.append(int(input('Введите число ')))
print(a)
for i in range(10):
    if a[i] > 5:
        b += a[i]
print(b)
