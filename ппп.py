p = ""
str = "123"
str2 = "678"

while True:
    p = input("Введите пароль")
    if len(p) <= 7:
        print("Пароль короткий")
    elif str in p:
        print("Пароль простой")
    elif str2 in p:
        print("Пароль простой")
    else:
        print("Пароль подходит")
        break
