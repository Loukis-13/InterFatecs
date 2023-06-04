try:
    while True:
        A, B = map(int, input().split())

        x = list(range(A))

        contador = B - 1
        while len(x) > 1:

            del x[contador]
            contador += B - 1
            contador %= len(x)

        print(x[0] + 1)

except EOFError:
    pass
