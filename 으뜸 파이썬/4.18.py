def sibal(n1,n2):
    import math
    numlist=[]
    for i in range(n1,n2+1):
        numlist.append(i)
        a=math.lcm(*numlist)
    print(a)

a=int(input())
b=int(input())
sibal(a,b)
