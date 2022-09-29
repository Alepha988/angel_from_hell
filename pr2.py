import math

x = float (input("Введите x "))
y = float (input("Введите y "))
z = float (input("Введите z "))
s = ((5*math.atan(x)-0.25*math.acos(x)*((x+3*abs(x-y) + x*x)))/((abs(x-y) *z + x*x)))
print("s= {0:.4}".format(s))
