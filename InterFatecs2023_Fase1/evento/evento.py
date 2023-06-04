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

    pontos = set([1])
    for i in range(1, N+1):
        if i in pontos:
            pontos.update(cidade[i])
            continue
        if len(pontos) == N:
            print("S")
            break
    else:
        if len(pontos) == N:
            print("S")
        else:
            print("N")

    # import pprint
    # pprint.pprint(cidade)
    
    # fila = [1]
    # visitados = set()

    # while fila:
    #     atual = fila.pop(0)

    #     if atual in visitados:
    #         continue

    #     visitados.add(atual)

    #     for i in cidade[atual]:
    #         fila.append(i)

    # if len(visitados) == N:
    #     print("S")
    # else:
    #     print("N")
        