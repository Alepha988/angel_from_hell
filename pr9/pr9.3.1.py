f = open('C:\\Users\\Alepha89\\PycharmProjects\\Yp\\Aleksey_Morgunov_vvod')
a = [line.replace("\n", "").split() for line in f]

flag = 1
for i in range(2):
    for j in range(i + 1, 2):
        if a[i][j] != a[j][i]:
            flag = 0

if flag == 1:
    print('Thats OK')
else:
    print('Not OK')

with open('C:\\Users\\Alepha89\\PycharmProjects\\Yp\\Aleksey_Morgunov_vivod','w') as f:
    if flag == 1:
        f.write('Thats OK')
    else:
        f.write('Not OK')
