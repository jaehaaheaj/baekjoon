def meetPtNum(s):
    x1, y1, r1, x2, y2, r2 = int(s[0]), int(s[1]), int(s[2]), int(s[3]), int(s[4]), int(s[5])
    dd = (x1 - x2)**2 + (y1 - y2)**2
    if(dd<r1**2 or dd<r2**2):
        val = (r1-r2)**2 - dd
        if(val>0):
            return 0
        elif(val==0):
            if(dd==0):
                return -1
            else:
                return 1
        else:
            return 2
    else:
        val = dd - (r1+r2)**2
        if(val>0):
            return 0
        elif(val==0):
            return 1
        else:
            return 2
    return 'error'

cnt = input()
for i in range(int(cnt)):
    s = input().split()
    print(meetPtNum(s))