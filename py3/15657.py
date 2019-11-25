n,m=map(int,input().split())
l=[int(i) for i in input().split()]
l.sort()

def f(s,i,x):
    if(x==0):
        print(s[:len(s)-1])
    else:
        for j in range(i,n):
            f(s+str(l[j])+' ',j,x-1)

f('',0,m)