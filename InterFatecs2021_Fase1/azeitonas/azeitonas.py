x, y = [int(i) for i in input().split(" ")]

if x < 1 or y < 1 or x == y:
    print("ERRO")
    exit(1)

print(x, y)
print(y, x)
print(y, -x)
print(x, -y)
print(-x, -y)
print(-y, -x)
print(-y, x)
print(-x, y)
