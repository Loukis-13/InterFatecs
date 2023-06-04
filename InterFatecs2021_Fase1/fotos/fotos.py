nk = []

try:
    while True:
        nk.append(int(input()))
except EOFError:
    pass

soma = sum(nk)

for i in nk:
    print("{:.3f}".format(round(i / soma, 3)))