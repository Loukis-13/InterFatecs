x, y, n = map(int, input().split())

impressora = [0 for _ in range(x)]
m = 0

for _ in range(n):
    a, b, c = map(int, input().split())

    for i in range(a, b):
        impressora[i] += c

        if impressora[i] > y:
            print("invalida")
            exit(0)

        if impressora[i] > m:
            m = impressora[i]
        
print(m)
