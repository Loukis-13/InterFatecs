input()
jogo = input()

pontuacao = [0,15,30,40,"ADV","GAME"]

w,x,u = 0,0,0
y,z,v = 0,0,0

def jogar(vitoria):
    global w,x,u,y,z,v
    if vitoria:
        u += 1
        if (u == 4 and v < 2) or u == 5:
            x += 1
            u = 0
            v = 0

        if (x == 6 and z <= 4):
            w += 1

        if v == 4:
            v -= 1
    else:
        v += 1
        if (v == 4 and u < 2) or v == 5:
            z += 1
            v = 0
            u = 0

        if (z == 6 and x <= 4):
            y += 1
                
        if u == 4:
            u -= 1
    
for i,j in enumerate(jogo):
    if i % 2 == 0:
        #jogador 1
        
        if j == "W":
            jogar(True)
        else:
            jogar(False)
        #     u += 1
        #     if (u == 4 and v < 2) or u == 5:
        #         x += 1
        #         u = 0
        #         v = 0

        #     if (x == 6 and z <= 4):
        #         w += 1
        # else:
        #     if u == 4:
        #         u -= 1
                
            
    else:
        #jogador2            
        if j == "W":
            jogar(False)
        else:
            jogar(True)
        #     v += 1
        #     if (v == 4 and u < 2) or v == 5:
        #         z += 1
        #         v = 0
        #         u = 0

        #     if (z == 6 and x <= 4):
        #         y += 1
        # else:
        #     if v == 4:
        #         v -= 1

print(f"{w} ({x}) [{pontuacao[u]}]-{y} ({z}) [{pontuacao[v]}]")