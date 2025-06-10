a = str(input("Введите текст"))
sogl = "цкнгшщзхфвпрлджчсмтб"
glas = "аеяоиэыю"
for c in glas:
    new = f'{c}к{c}'
    a = a.replace(c, new)
for d in sogl:
    new2= f'{d}ъ{d}'
    a = a.replace(d, new2)
print(a)