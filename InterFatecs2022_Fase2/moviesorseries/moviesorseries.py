# python moviesorseries/moviesorseries.py < moviesorseries/input/1.txt > moviesorseries/result/1.txt
# diff moviesorseries/output/1.txt moviesorseries/result/1.txt

h = 26
i = 29

while True:
    d = int(input())
    
    if d == 0:
        break
    elif d == 98:
        print("IAN BIRTHDAY, GO OUT FOR DINNER")
        i += 1
    elif d == 99:
        print("HELLEN BIRTHDAY, GO OUT FOR DANCING")
        h += 1
    else:
        m = int(input())
        if (d + m + h + i)%2:
            print("WATCH MOVIE")
        else:
            print("WATCH SERIES")
