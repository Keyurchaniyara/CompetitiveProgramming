def nbythree(n):
    l = len(n)//3
    count = 0
    di = {}
    for i in n:
        di[i] = n.count(i)

    print(max(di, key=di.get))

n = [10, 10, 20, 30, 30, 30]
nbythree(n)