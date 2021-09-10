inp = input("enter the string :-- ")
def consonants(s):
    l2 = []
    for j in s:
        l2.append(j)
    Counter = 0
    l = ['a','e','i','o','u']
    for i in l2:
        if i in l:
            Counter += 1
    return Counter

s1 = consonants(inp)
print(s1)