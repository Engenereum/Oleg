fname = input("Введите имя файлв")
f = open(fname, encoding='utf-8')
src = f.read()
words = src.split(' ')
r = {}
for word in words:
    word = word.replace('(', '').replace(')', '').strip().lower()
    if word == '':
        continue
    if word in r.keys():
        r[word] += 1
    else:
        r[word] = 1
max_repeat = max(r.values())
for k, v in r.items():
    if v == max_repeat:
        print(k, v)
        break
