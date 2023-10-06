n = int(input())

candidatos = dict()

for i in range(n):
    G, E, A, B, T = map(int, input().split())

    if not (G and E) and not (A or (B and G)):
        print(f"Cand. {i+1}: INDEFERIDO (acad)")
    elif T >= 3 and (A or (B and G)):
        print(f"Cand. {i+1}: deferido (comprovar 3 anos)")
    elif (T == 5) and G and E:
        print(f"Cand. {i+1}: deferido (comprovar 5 anos)")
    else:
        print(f"Cand. {i+1}: INDEFERIDO (exp)")
