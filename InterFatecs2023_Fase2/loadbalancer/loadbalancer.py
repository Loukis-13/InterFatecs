n = int(input())
n_reqs = int(input())
x = int(input())

reqs = [[*map(int, input().split()), i+1] for i in range(n_reqs)]

reqs.sort()

servers = [[] for _ in range(n)]
clock = 1

for t, time, alvo in reqs:
    for i in servers:
        i[:] = [v for j in i if (v := j - (t - clock)) > 0]

    i = servers.index(min(servers, key=len))

    if alvo == x:
        print(i+1)
        break

    servers[i].append(time)

    clock = t
