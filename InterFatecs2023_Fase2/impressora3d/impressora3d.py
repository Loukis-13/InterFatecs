x, y, n = map(int, input().split())

impressora = [0 for _ in range(x+2)]

for _ in range(n):
    a, b, c = map(int, input().split())

    impressora[a] += c
    impressora[b] -= c

s, m = 0, 0
for i in impressora:
    s += i
    m = max(s, m)

    if m > y:
        print("invalida")
        break
else:
    print(m)
