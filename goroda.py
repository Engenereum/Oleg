stop = ""
t1 = input("Введите первый город").lower()
while stop != "exit":
    t2 = input("Введите второй город").lower()
    if t1[-1] == t2[0]:
        print("Верный город")
        t1 = t2
    else:
        print("Неверный город")
    stop = input("Продолжить? Выход - exit")