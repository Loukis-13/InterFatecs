n = int(input())

candidatos = dict()

for i in range(n):
    G, E, A, B, T = map(int, input().split())

    if T == 2:
        print(f"Cand. {i+1}: INDEFERIDO (exp)")
    elif T > 2 and (A or B) and G:
        print(f"Cand. {i+1}: deferido (comprovar 3 anos)")
    elif T == 5 and G and E:
        print(f"Cand. {i+1}: deferido (comprovar 5 anos)")
    else:
        print(f"Cand. {i+1}: INDEFERIDO (acad)")
