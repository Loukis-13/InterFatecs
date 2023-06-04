h, w, bateria = map(int, input().split())

y, x = map(int, input().split())

comandos = input()

batidas = 0

for i in comandos[:bateria]:
    if i == "C" and 0 < y-1:
        y -= 1
    elif i == "B" and y+1 <= h:
        y += 1
    elif i == "E" and 0 < x-1:
        x -= 1
    elif i == "D" and x+1 <= w:
        x += 1
    else:
        batidas += 1

print(y, x, batidas)
