n = int(input())
n_reqs = int(input())
x = int(input())

reqs = [[*map(int, input().split()), i+1] for i in range(n_reqs)]

reqs.sort()

servers = [0 for i in range(n)]
clock = 1

for t, time, alvo in reqs:
    i = servers.index(min(servers))

    servers = [max(0, i - t) for i in servers]

    if alvo == x:
        print(i+1)
        break

    servers[i] += time

    clock = i
