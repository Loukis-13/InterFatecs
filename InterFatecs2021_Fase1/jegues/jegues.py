competidores = []

try:
    while True:
        competidores.append(input().split())
          
except EOFError:
    pass

competidores.sort(key=lambda x: int(x[1]))
print("T1", competidores[0][0], competidores[1][0], competidores[2][0])

competidores.sort(key=lambda x: int(x[2]))
print("T2", competidores[0][0], competidores[1][0], competidores[2][0])

competidores.sort(key=lambda x: int(x[3]))
print("CHEGADA", competidores[0][0], competidores[1][0], competidores[2][0])