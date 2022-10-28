def fig(a,b,h):
	s1= 1/2 * a * h
	print('Площадь треугольника равна ', s1)
	s2 = a*a
	print ('Площадь квадрата равна ', s2)
	s3 = (a+b)/2 * h
	print ('Площадь трапеции равна ', s3)
	return s1, s2, s3
x = int(input('Введите сторону а:'))
y = int(input('Введите сторону y:'))
z = int(input('Введите сторону z:'))
print(fig(x,y,z))
