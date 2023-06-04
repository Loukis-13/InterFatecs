while (x := int(input())) != 0:
    print(*(i**2 for i in range(1, int(x**.5)+1)))
