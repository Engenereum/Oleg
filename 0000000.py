scr = "387482737ос47274243741248718941713984873710"
scr2 = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
for i in scr:
    if i in scr2.keys():
        scr2[i] += 1
print(scr2)

books = {"Математика": 12, "Русский язык": 144, "История": 17}
res = 99999999999999999999999999999999
b = ""
for a in books.keys():
    # res += books[a]
    if books[a] < res:
        b = a
        res = books[a]

print(b)
