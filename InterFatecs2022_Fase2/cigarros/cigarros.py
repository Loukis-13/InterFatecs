while True:
    n, k = map(int, input().split())
    
    if n == k == 0:
        break
        
    c = n
    bitucas = n
    
    while bitucas >= k:
        c += bitucas // k
        bitucas = bitucas // k + bitucas % k
        
    print(c)
    