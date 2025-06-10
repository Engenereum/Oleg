scr = "Задание на неделю"
a = []
b = []
for ch in scr:
    if ch in a:
        index = a.index(ch)
        b[index] += 1
    else:
        a.append(ch)
        b.append(1)
print(a)
print(b)

print("-----------------------------------------------------------------------------------------------------------------------------")

str1 = "воашо шаов аышвоаы0уаоо ца0а ывоа ыощшавещ н шш шш ш шш ш ш ш шш ш шшш шшщ  шупоупщ"
str2 = []
str3 = []

for index in range(0, len(str1), 1):
    if index % 2 == 0:
        str2.append(str1[index])
    else:
        str3.append(str1[index])
str2 = str(str2).replace("'", "").replace(", ", "").replace("]", "").replace("[", "")
str3 = str(str3)
print(str2)
print(str3)

print("-----------------------------------------------------------------------------------------------------------------------------")

src = "3р4о53л5р6р643ш6шо3л463од6о43ш6ш34щ6ошр4р6и36иисрыщ35ш3щ4з63рш6ищ"
numbers = [str(v) for v in list(range(0, 10, 1))]
counts = [0,0,0,0,0,0,0,0,0,0]

for l in src:
    if l in numbers:
        index2 = numbers.index(l)
        counts[index2] += 1
print(numbers)
print(counts)