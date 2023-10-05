n = int(input())
code = input()

for i in range(len(code)-n+1):
    if code[i:i+n] == code[i:i+n][::-1]:
        print("S")
        break
else:
    print("N")
