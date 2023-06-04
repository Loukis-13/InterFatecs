n = int(input())
for _ in range(n):
    l1, l2, l3 = False, False, False
    texto = input()
    res = ""

    def L2():
        global l2
        l2 = not l2
        return "E" if not l2 else "D"

    for i in texto:
        if i == "A":
            if not l1:
                res += "D"
            else:
                res += L2()
            l1 = not l1
        elif i == "B":
            res += L2()
        elif i == "C":
            if l3:
                res += "E"               
            else:
                res += L2()
            l3 = not l3

    print(res)