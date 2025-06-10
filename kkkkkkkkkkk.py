def func(oleg):
    return oleg.upper()


a = "Oleg"
b = func(a)

print(b)


def s(num, num2, z, ):
    if z == "+":
        return num + num2
    elif z == "-":
        return num - num2
    elif z == "*":
        return num * num2
    elif z == "/":
        return num / num2


a2 = 6
b2 = 2
c2 = '*'
d2 = s(a2, b2, c2)
print(d2)


def scr(src, src2):
    if len(src) > len(src2):
        return src
    elif len(src2) > len(src):
        return src2


a3 = 'trtrtyrdytyrdtdyt'
b3 = 'rdtvhnilrtsoeuosev'
c3 = scr(a3, b3)
print(c3)


def skd(st, si):
    res = 0
    for char in st:
        if si == char:
            res += 1
    return res


e = 'ваывшоашывашыоущшсьфцругсьфцяадгслтаслвапкмтя'
f = 'в'
g = skd(e, f)
print(g)


def kor(i):
    return len(i)
m = ("helloh")
m2 = kor(m)
print(m2)