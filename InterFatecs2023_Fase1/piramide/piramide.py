import string

n, case = input().split()
n = int(n)

alpha = string.ascii_uppercase if case == "maiusculas" else string.ascii_lowercase

for i in range(n):
    print(f"{alpha[:i+1]:.>26}")
    