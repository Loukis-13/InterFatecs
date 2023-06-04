import string

CODIGO_BASE = f"-{string.ascii_lowercase}."

while (f := input()) != "0":
    k, f = f.split()
    k = int(k)

    n = len(f)
    codigo_base = [0 for _ in range(n)]
    codigo_cifrado = [CODIGO_BASE.index(i) for i in f]

    for i in range(n):
        codigo_base[(k*i)%n] = (codigo_cifrado[i] + i) % 28

    print("".join(CODIGO_BASE[i] for i in codigo_base))


"""
crypt cat <-> cs.

c -> c | 3 -> 3
cf = (codigo_base[(k*i) % n] - i) % 28
cf = (codigo_base[(5*0) % 3] - 0) % 28
cf = (codigo_base[0] - 0) % 28
cf = (3 - 0) % 28
cf = 3

c <- c | 3 <- 3
cf = (codigo_base[(k*i) % n] - i) % 28
3 = (codigo_base[(5*0) % 3] - 0) % 28
3 = (codigo_base[0] - 0) % 28
3 = codigo_base[0] % 28
3 % 28 = codigo_base[0]
3 = codigo_base[0]


a -> s | 1 -> 19
cf = (codigo_base[(k*i) % n] - i) % 28
cf = (codigo_base[(5*1) % 3] - 1) % 28
cf = (codigo_base[2] - 1) % 28
cf = (20 - 1) % 28
cf = 19 % 28
cf = 19

a <- s | 1 <- 19
cf = (codigo_base[(k*i) % n] - i) % 28
19 = (codigo_base[(5*1) % 3] - 1) % 28
19 = (codigo_base[2] - 1) % 28
19 = codigo_base[2] % 28 - 1 % 28
19 = codigo_base[2] % 28 - 1
19 + 1 = codigo_base[2] % 28
20 % 28 = codigo_base[2]
20 = codigo_base[2]


t -> . | 20 -> 27
cf = (codigo_base[(k*i) % n] - i) % 28
cf = (codigo_base[(5*2) % 3] - 2) % 28
cf = (codigo_base[10 % 3] - 2) % 28
cf = (codigo_base[1] - 2) % 28
cf = (1 - 2) % 28
cf = -1 % 28
cf = 27

t <- . | 20 <- 27
cf = (codigo_base[(k*i) % n] - i) % 28
27 = (codigo_base[(5*2) % 3] - 2) % 28
27 = (codigo_base[10 % 3] - 2) % 28
27 = (codigo_base[1] - 2) % 28
27 = codigo_base[1] % 28 - 2 % 28
27 = codigo_base[1] % 28 - 2
27 + 2 = codigo_base[1] % 28
29 = codigo_base[1] % 28
29 % 28 = codigo_base[1]
1 = codigo_base[1]
"""
