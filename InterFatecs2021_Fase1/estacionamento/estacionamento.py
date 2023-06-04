estacionamento = [0] * 15

try:
    while True:
        placa = input()
        acc = sum(ord(i) for i in placa)

        if estacionamento[acc % 15] == 0:
            estacionamento[acc % 15] = placa
          
except EOFError:
    pass

for i, v in enumerate(estacionamento, 1):
    if v: 
        print(i, v)
