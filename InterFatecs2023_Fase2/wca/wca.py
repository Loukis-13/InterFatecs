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

    x /= len(temps)

    horas = x//60_000

    return (str(horas) if horas else "") + f"{int(x//1000%60):02}:{int(x%1000):>03}"


print(".Id.Nome.......................Media......Melhor")

while (ent := input()) != "FIM":
    n, cubo = ent.split(maxsplit=1)

    print(cubo)

    cubo = []

    for i in range(int(n)):
        equipe, *tempos = input().split()

        media = ""
        melhor = ""

        tempos.sort()

        DNFs = tempos.count("0:00:000")

        if DNFs == 0:
            melhor = calc_temp([tempos[0]])
            media = calc_temp(tempos[1:4])
        elif DNFs == 1:
            melhor = calc_temp([tempos[1]])
            media = calc_temp(tempos[2:])
        elif 2 <= DNFs <= 4:
            media = "DNF"
            while "0:00:000" in tempos:
                tempos.remove("0:00:000")
            melhor = calc_temp([tempos[0]])
        else:
            media = "DNF"
            melhor = "DNF"

        cubo.append([media, melhor, participantes[equipe], equipe])

    cubo.sort()

    for media, melhor, equipe, id in cubo:
        print(f"{id:>3} {equipe:<20}{media:>12}{melhor:>12}")
