# python terminus.py < in/2.in | diff - out/2.out 
# from pprint import pprint

terminais = ["" for _ in range(7)]
# espera = set()
naves = dict()

total = []

def calc(nave):
    taxa = 1 + (0.07 * (nave["trocas"] > 1)) + (0.05 * (nave["espera?"]))
    return round((nave["saida"] - nave["entrada"]) / 123.457 * 4.59 * taxa, 2)

try:
    while True:
        nave, terminal, tempo = input().split()
        
        term = int(terminal)-1
        
        if nave not in naves:
            naves[nave] = {
                "entrada": int(tempo),
                "saida": 0,
                "terminal": 0,
                "trocas": 0,
                "espera?": False
            }

        if terminal != "0":
            naves[nave]["terminal"] = term
            naves[nave]["trocas"] += 1

            if terminais[term] == "":
                terminais[term] = nave
                
            elif "" in terminais:
                term = terminais.index("")
                terminais[term] = nave

                naves[nave]["espera?"] = True
                naves[nave]["terminal"] = term
                naves[nave]["trocas"] += 1
                
            # else:
            #     # espera.add(nave)
            #     naves[nave]["espera?"] = True
        else:
            naves[nave]["saida"] = int(tempo)
            terminais[naves[nave]["terminal"]] = ""

            tot = [int(tempo), nave, f"{calc(naves[nave]):.2f}"]
            s = []

            if naves[nave]["espera?"]:
                s.append("E")
            if naves[nave]["trocas"] > 1:
                s.append("X")

            if s:
                tot.append(" ".join(s))

            total.append(tot)

            del naves[nave]
            # espera.discard(nave)
            
        # print(terminais)
        # print(espera)
        # pprint(naves)
        # print()
except EOFError:
    pass

for i in total:
    print(*i[1:])
