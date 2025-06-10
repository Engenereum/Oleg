t1 = input("введите первый город").upper()
t2 = input("введите второй город").upper()
if t1[-1] == t2[0]:
    print("Верно")
else:
    print("Ошибка")