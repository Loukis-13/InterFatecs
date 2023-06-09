while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break
    
    cidade = {i+1: set() for i in range(N)}

    for _ in range(M):
        V, W, D = map(int, input().split())

        cidade[V].add(W)
        if D == 2:
            cidade[W].add(V)
    

    for i in range(1, N+1):
        fila = [i]
        visitados = {i,}

        while fila:
            atual = fila.pop(0)

            for i in cidade[atual]:
                if i not in visitados:
                    fila.append(i)
                    visitados.add(i)

        if len(visitados) != N:
            print("N")
            break
    else:
        print("S")
        