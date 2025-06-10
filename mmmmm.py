
a = input("Введите текст для шифрования")
i = 0
while i < len(a):
    if i == len(a) - 1:
        print(ord(a[i]))
    else:
        print(ord(a[i]), end=', ')
    i += 1


b = ', '
out = a.join
print(out)

for v in a:
    print(ord(v))
