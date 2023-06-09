poder = int(input())
h, w = map(int, input().split())

inicio, fim = None, None
campo = []
for i in range(h):
    linha = input().split()

    if "S" in linha:
        inicio = (linha.index("S"), i)
    if "K" in linha:
        fim = (linha.index("K"), i)

    campo.append(linha)


fila = [inicio]
distancia = {inicio: 0}

while fila:
    atual = fila.pop(0)

    if atual == fim:
        print(distancia[atual])
        break

    x, y = atual

    for ix, iy in [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]:
        if not 0 <= ix < w or not 0 <= iy < h or campo[iy][ix] == "#":
            continue
            
        if campo[iy][ix].isnumeric() and int(campo[iy][ix]) > poder:
            continue
        
        if (ix, iy) not in distancia or distancia[atual] + 1 < distancia[(ix, iy)]:
            fila.append((ix, iy))
            distancia[(ix, iy)] = distancia[atual] + 1
else:
    print("N")
