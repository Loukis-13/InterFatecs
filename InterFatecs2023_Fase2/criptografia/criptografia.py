users = []

while (inp := input()) != "ACABOU":
    user, passwd = inp.split()

    s = sum(ord(c) * i for i, c in enumerate(passwd, 1))

    hash = str(s)

    while s > 1:
        x = s

        if s%2==0:
            x = 2
        else:
            for i in range(3, int(s**.5)+1, 2):
                if s%i == 0:
                    x = i
                    break

        hash += str(x)
        s //= x

    users.append((user, hash))

users.sort()

for u, s in users:
    print(f"usuario...: {u}")
    print(f"valor hash: {s}")
    print("------------------------------")
