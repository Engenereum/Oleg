a = {0: "Первый элемент", 1: "Второй элемент"}
b = {2: "авав", 3: "23398414"}
print(a)
print(a[0])
a[123] = "ПРивеет"
print(a)
del a[1]
print(a)
print(a.keys())
print(list(a.keys()))

for key, value in a.items():
    print(key, value)
