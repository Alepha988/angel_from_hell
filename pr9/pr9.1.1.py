f = open('C:\\Users\\Alepha89\\PycharmProjects\\Yp\\Aleksey_Morgunov_vvod')
a = [line.replace("\n", "").split() for line in f]
k = 0
s = 0
for i in range(N):
	for j in range(N):
		if i < j:
			s = s + a[i][j]
		if a[i][j] > 0:
			k += 1
with open('C:\\Users\\Alepha89\\PycharmProjects\\Yp\\Aleksey_Morgunov_vivod','w') as f:
	f.write('Сумма элементов над главной диагональю: ')
	f.write(s)
	f.write('Кол-во положительных элементов')
	f.write(k)
