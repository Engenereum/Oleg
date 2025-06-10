a = input("Введите оценки")
a = a.split(',')
for i in range(len(a)):
    a[i] = int(a[i])
b = (sum(a) / len(a))
if b >= 4.5:
    print("Вы отличник")
elif b >= 3.5:
    print("Вы хорошист")
elif b >= 2.5:
    print("Вы троечник")
else:
    print("Вы двоечник")
