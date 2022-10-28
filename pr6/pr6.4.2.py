from random import randint

a = [] 
b = []
for i in range(10):
	a.append(int(input('Введите числа\n')))
print(a)
for i in range(10):
	if a[i] % 2 != 0:
		b.append(a[i])
if b == []:
	print('Нечётных чисел нет')
else:
	b.sort(reverse=True)
	print(b)
