n,m=map(int,input().split())
cl=[int(i) for i in input().split()]
cl += cl[:3]
pl = [cl[i]*cl[i+1]*cl[i+2]*cl[i+3] for i in range(n)]
s = sum(pl)
pl = pl[len(pl)-3:]+pl
for i in input().split():
    for j in range(4):
        k = (int(i)-1+j)%n
        pl[k] *= -1
        s += pl[k]*2
    print(s)