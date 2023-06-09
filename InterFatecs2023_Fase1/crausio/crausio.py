h, w, bateria = map(int, input().split())

x, y = map(int, input().split())

comandos = input()

batidas = 0

for i in comandos[:bateria]:
    if i == "C" and 0 < x-1:
        x -= 1
    elif i == "B" and x+1 <= h:
        x += 1
    elif i == "E" and 0 < y-1:
        y -= 1
    elif i == "D" and y+1 <= w:
        y += 1
    else:
        batidas += 1

print(x, y, batidas)
