a, b = [int(i) for i in input().split(' ')]
x = int(b/a*100)
if(x>=99):
    print(-1)
else:
    import math
    print(math.floor((a*(x+1)-b*100)/(100-x-1))+1)