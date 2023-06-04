N_EMP, Q_PAD = map(int, input().split())
dias = int(input())

botijoes = {i: {j:0 for j in set(range(1, N_EMP+1)) - {i,}} for i in range(1, N_EMP+1)}

for d in range(1, dias+1):
    input()
    for _ in range(N_EMP**2 - N_EMP):
        e1, e2, q = map(int, input().split())

        botijoes[e1][e2] += q
        
    print(f"Final dia {d}")
    flag = True
    for i in range(1, N_EMP+1):
        for j in set(range(1, N_EMP+1)) - {i,}:
            if botijoes[i][j] >= Q_PAD and botijoes[j][i] >= Q_PAD:
                flag = False
                print(f"  Trocas entre {i}({botijoes[i][j]//Q_PAD}v) e {j}({botijoes[j][i]//Q_PAD}v)")
                botijoes[i][j] %= Q_PAD
                botijoes[j][i] %= Q_PAD

    if flag:
        print("  Sem Trocas")