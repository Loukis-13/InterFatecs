s = int(input().split()[0])
p = 1

c = input().split()
c.sort(key="TRS".index)

for i in c:
    if i == "T":
        p += 1
    elif i == "R":
        p += s//2
    elif i == "S" and s > 3 and p > 1:
        s -= 1
        p += p//2
    else:
        break
    
print(p*s)
