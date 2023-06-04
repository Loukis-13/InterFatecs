n = int(input())
a, b = map(int, input().split())
c, d = map(int, input().split())
lab = [input() for _ in range(n)]

fila = [(a, b)]
caminhos = {(a, b): None}

while fila:
    atual = fila.pop(0)
    y, x = atual
    if atual == (c, d):
        break

    for y, x in [(y, x+1), (y+1, x), (y, x-1), (y-1, x)]:
        if 0 <= x-1 < n and 0 <= y-1 < n and lab[y-1][x-1] == "1" and (y, x) not in caminhos:
            fila.append((y, x))
            caminhos[(y, x)] = atual

caminho = [(c, d)]
x = (c, d)
while x := caminhos[x]:
    caminho.append(x)

for i in caminho[::-1]:
    print(*i)
