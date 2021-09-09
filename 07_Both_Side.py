def both_side(l,n):
    if n%2==0:
        s=0
        for i in range(n//2):
            n = l[-1]+l[0]
            s += n
            l.pop(-1)
            l.pop(0)
        print(s)
    else:
        s=0
        for i in range(n//2):
            n = l[-1]+l[0]
            s += n
            l.pop(-1)
            l.pop(0)
        if l[0]>l[-1]:
            s += l[0]
        else:
            s += l[-1]
        print(s)
        
l = [1,7,10,4,5,6,9,8,3,4,1,3,4,5]
n = int(input("B :--"))
both_side(l,n)