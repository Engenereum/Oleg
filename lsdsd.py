list1 = input("Введите первый список")
list2 = input("Введите второй список")
a = sorted(list1)
b = sorted(list2)
if len(a) > len(b):
    print("Список 1 длинее")
elif len(a) < len(b):
    print("Список 2 длинее")
