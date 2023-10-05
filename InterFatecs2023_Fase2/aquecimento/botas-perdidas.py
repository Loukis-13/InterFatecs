botas = []

trans = str.maketrans("ED", "DE")

n = 0
for _ in range(int(input())):
    bota = input()
    par = bota.translate(trans)

    if par in botas:
        n += 1
        botas.remove(par)
    else:
        botas.append(bota)

print(n)
