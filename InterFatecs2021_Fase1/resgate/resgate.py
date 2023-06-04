N, R, S = map(int, input().split())

input()
T = set(map(int, input().split()))

comodos = {i+1: [] for i in range(N)}

for _ in range(int(input())):
    c1, c2 = map(int, input().split())

    if c1 not in T and c2 not in T:
        comodos[c1].append(c2)
        comodos[c2].append(c1)

fila = [R]
visitados = {R,}

while fila:
    atual = fila.pop(0)
    if atual == S:
        print("PROSSEGUIR")
        break

    for i in comodos[atual]:
        if i not in visitados:
            fila.append(i)
            visitados.add(i)
            
else:
    print("ABORTAR")        
