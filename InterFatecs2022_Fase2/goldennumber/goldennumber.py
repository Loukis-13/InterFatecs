# python goldennumber/goldennumber.py
# python goldennumber/goldennumber.py < goldennumber/input/1.txt > goldennumber/result/1.txt
# diff goldennumber/output/1.txt goldennumber/result/1.txt

r = 1
for i in range(int(input())):
    r = 1 + (1/r)
print("{:.15f}".format(r))

# print("{:.15f}".format(__import__('functools').reduce(lambda acc, _: 1 + (1/acc), [1]*int(input()), 1)))