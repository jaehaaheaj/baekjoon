'''
(x^2 - 2x1x + x1^2) + (y^2 - 2y1y + y1^2) = r1^2
(x^2 - 2x2x + x2^2) + (y^2 - 2y2y + y2^2) = r2^2

circle equation
(x^2 - (x1 + x2)x + (x1^2 + x2^2)/2) + (y^2 - (y1 + y2)x + (y1^2 + y2^2)/2) = (r1^2 + r2^2)/2
(x-(x1+x2)/2)^2 + (y-(y1+y2)/2)^2 - ((x1+x2)/2)^2 - ((y1+y2)/2)^2 + (x1^2 + x2^2)/2 + (x1^2 + x2^2)/2 = (r1^2 + r2^2)/2
(x-(x1+x2)/2)^2 + (y-(y1+y2)/2)^2 = ((x1+x2)/2)^2 + ((y1+y2)/2)^2 - (x1^2 + x2^2)/2 - (x1^2 + x2^2)/2 + (r1^2 + r2^2)/2

line equation
(x1^2 - x2^2 - 2(x1-x2)x) + (y1^2 - y2^2 - 2(y1-y2)y) = r1^2 - r2^2
2(x1-x2)x + 2(y1-y2)y = (x1^2 - x2^2) + (y1^2 - y2^2) - (r1^2 - r2^2)

circle meets line? check dist btw circle center and line.
2 or 1 or 0
'''

def radiusCheck(s):
    x1, y1, r1, x2, y2, r2 = int(s[0]), int(s[1]), int(s[2]), int(s[3]), int(s[4]), int(s[5])
    return ((x1+x2)/2)**2 + ((y1+y2)/2)**2 - (x1**2 + x2**2)/2 - (y1**2 + y2**2)/2 + (r1**2 + r2**2)/2

cnt = input()
for i in range(int(cnt)):
    s = input().split()
    r = radiusCheck(s)
    print(r)
    if(r<0):
        print(0)
    elif(r==0):
        print(1)
    else:
        print(2)