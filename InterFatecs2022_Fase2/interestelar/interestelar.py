# ./teste.sh interestelar
N = int(input())
L, U = map(int, input().split())

R = int(N**0.5)

planetas = [L <= int(input()) <= U for i in range(N)]
seq = [sum(planetas[i:i+R]) for i in range(0, N, R)]

try:
    while True:
        x, y = map(int, input().split())

        if x == y:
            print(int(planetas[x]))
            continue

        div_x, res_x = divmod(x, R)
        div_x += 1
        div_y, res_y = divmod(y, R)
        div_y += 1

        contador = sum(seq[div_x : div_y])

        if res_x:
            contador += sum(planetas[x: x+res_x])
        if res_y:
            contador += sum(planetas[y-res_y: y+1])
        
        print(contador)
except EOFError:
    pass
