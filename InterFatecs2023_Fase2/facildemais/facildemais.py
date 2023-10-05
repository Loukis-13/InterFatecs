n = int(input())

impar = 0

for _ in range(n):
    if input() != "1":
        impar += 1

print("impar" if impar%2 else "par")
