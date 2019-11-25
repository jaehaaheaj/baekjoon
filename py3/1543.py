s = input()
ss = input()
v = 0
while(True):
    i = s.find(ss)
    if(i==-1):
        print(v)
        break
    else:
        s = s[i+len(ss):]
        v+=1