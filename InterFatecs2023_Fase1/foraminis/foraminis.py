HG = 1/2**0.5

for _ in range(int(input())):
    S = [*map(int, input().split())]

    LF = [S[i] * HG + S[i+1] * HG for i in range(0, 8, 2)]

    ES = sum(i**2 for i in S)
    ELF = sum(i**2 for i in LF)

    print("INIMIGO" if ELF and (ELF/ES) > .5 else "-")
    