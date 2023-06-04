# ./teste.sh peraaitalidandoerrado

import math
while (n := int(input())) != 0:
    n = int(input())

    if n == 0:
        break

    x = math.sqrt(n)
    if x.is_integer():
        print(int(x*2 - 1))
    else:
        print("PERA AI... TA LIDANDO ERRADO!")
