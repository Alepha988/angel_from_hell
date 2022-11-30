import math

print('Блок А, номер 1')
x = int(input())
n = int(input())

def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n

x = pow(x, n)
print(x / factorial(n))

print('Блок Б, номер 1')

def function():
    a = int(input())
    if a == 0:
        return 0
    else:
        return max(a, function())

print(function())
