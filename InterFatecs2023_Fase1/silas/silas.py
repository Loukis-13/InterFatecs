poder = int(input())

h, w = map(int, input().split())

campo = [input().split() for _ in range(h)]

h -= 1
w -= 1

fila = [(0, 0)]
distancia = {(0, 0): 0}
visitados = set()

ultimo = (0, 0)

while fila:
    atual = fila.pop(0)
    x, y = atual

    if campo[y][x] == "K":
        print(distancia[atual])
        break

    visitados.add(atual)

    for ix, iy in [(x, y+1), (x+1, y)]:
        if ix > w or iy > h or campo[iy][ix] == "#" or (ix, iy) in visitados:
            continue
            
        if campo[iy][ix].isnumeric() and int(campo[iy][ix]) > poder:
            continue
                
        fila.append((ix, iy))
        visitados.add((ix, iy))
        distancia[(ix, iy)] = distancia[atual] + 1
else:
    print("N")
            