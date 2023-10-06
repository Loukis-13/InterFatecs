n = int(input())

participantes = dict()
for _ in range(n):
    i, part = input().split(maxsplit=1)
    participantes[i] = part

cubos = dict()

def calc_temp(temps):
    x = 0
    for i in temps:
        i = tuple(map(int, i.split(":")))
        x += i[0] * 60_000 + i[1] * 1000 + i[2]

    x //= len(temps)

    horas = int(x//60_000)

    return x, (f"{horas}:" if horas else "") + f"{int(x//1000%60):02}:{int(x%1000):>03}"


print(".Id.Nome.......................Media......Melhor")

while (ent := input()) != "FIM":
    n, cubo = ent.split(maxsplit=1)

    print(cubo)

    cubo = []

    for i in range(int(n)):
        equipe, *tempos = input().split()

        media = "DNF"
        melhor = "DNF"
        pos_1 = float("inf")
        pos_2 = float("inf")

        tempos.sort()

        DNFs = tempos.count("0:00:000")

        if DNFs == 0:
            pos_1, media = calc_temp(tempos[1:4])
            pos_2, melhor = calc_temp([tempos[0]])
        elif DNFs == 1:
            pos_1, media = calc_temp(tempos[2:])
            pos_2, melhor = calc_temp([tempos[1]])
        elif 2 <= DNFs <= 4:
            while "0:00:000" in tempos:
                tempos.remove("0:00:000")
            pos_2, melhor = calc_temp([tempos[0]])

        cubo.append([pos_1, pos_2, media, melhor, participantes[equipe], equipe])

    cubo.sort()

    for *_, media, melhor, equipe, id in cubo:
        print(f"{id:>3} {equipe:<20}{media:>12}{melhor:>12}")
