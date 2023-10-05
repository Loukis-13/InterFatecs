from pprint import pprint


terminais = ["" for _ in range(7)]
naves = dict()
total = []
fila = []

try:
    while True:
        nave, terminal, tempo = input().split()
        tempo = int(tempo)
        terminal = int(terminal)-1
        
        if nave not in naves:
            naves[nave] = {
                "entrada": tempo,
                "saida": 0,
                "terminal": terminal,
                "trocou?": False,
                "espera?": False
            }

        if terminal != -1:
            if naves[nave]["terminal"] != terminal:
                naves[nave]["trocou?"] = True
                naves[nave]["terminal"] = terminal

            if terminais[terminal] == "":
                terminais[terminal] = nave
                
                # if naves[nave]["entrada"] == 0:
                #     naves[nave]["entrada"] = tempo
                
            # elif "" in terminais:
            #     terminal = terminais.index("")
            #     terminais[terminal] = nave

            #     naves[nave]["espera?"] = True
            #     naves[nave]["terminal"] = terminal
            #     naves[nave]["trocas"] += 1

            else:
                fila.append(nave)
                naves[nave]["espera?"] = True
        else:
            nave_ = naves[nave]
            naves[nave]["saida"] = tempo
            terminais[naves[nave]["terminal"]] = ""

            taxa = 1 + (0.07 * nave_["trocou?"]) + (0.05 * (nave_["espera?"]))
            
            tot = [tempo, nave, f"{(nave_['saida'] - nave_['entrada']) / 123.457 * 4.59 * taxa:.2f}"]

            if nave_["espera?"]:
                tot.append("E")
            if nave_["trocou?"]:
                tot.append("X")
            
            total.append(tot)

            del naves[nave]
            
            if nave in fila:
                fila.remove(nave)

        if fila and "" in terminais:
            terminal = terminais.index("")
            nave = fila.pop(0)
            terminais[terminal] = nave

            # if naves[nave]["entrada"] == 0:
            #     naves[nave]["entrada"] = tempo

            if naves[nave]["terminal"] != terminal:
                naves[nave]["trocou?"] = True

            naves[nave]["terminal"] = terminal
            

        # print(terminais)
        # print(fila)
        # pprint(naves)
        # print()
except EOFError:
    pass

total.sort()

for i in total:
    print(*i[1:])


