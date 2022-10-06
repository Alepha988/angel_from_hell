s=input('Введите строку ')
print(s.count('.'))
print(s.translate({ord('.'):('')}))
