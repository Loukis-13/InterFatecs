import re

try:
    while True:
        s = re.sub(r"[^a-z0-9]", "", input().casefold())
        
        if s == s[::-1]:
            print("Parabens, voce encontrou o Palindromo Perdido!")
        else:
            print("A busca continua, o Palindromo Perdido ainda nao foi encontrado.")
except EOFError:
    pass