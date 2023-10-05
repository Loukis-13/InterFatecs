from collections import defaultdict

n = int(input())

deps = defaultdict(set)

for _ in range(n):
    x, y = input().split()

    deps[x].add(y)

def check(x, coll):
    for i in deps[x]:
        if i in coll:
            return False
        elif i in deps and not check(i, coll | set(i)):
            return False
    return True

for k in deps:
    if not check(k, set(k)):
        print("usar injecao tardia")
        break
else:
    print("ok")
