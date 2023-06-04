n = int(input())


for _ in range(n):
    contador = 0

    s1 = input()
    s2 = sorted(input())

    if len(s2) > len(s1):
        print("ERRO")
        continue

    for i in range(len(s1) - (len(s2) - 1)):
        if s2 == sorted(s1[i : i + len(s2)]):
            contador += 1

    print(contador)
