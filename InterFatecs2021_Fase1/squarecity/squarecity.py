n = int(input())
x = 0

for i in range(3, n+1, 4):
    x += i*4-6

print(x)

# print(sum(i*4-6 for i in range(3, int(input())+1, 4)))