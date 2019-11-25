n = int(input())
if(n<3):
    print(1)
else:
    a,b,c=1,1,2
    for _ in range(n-3):
        a,b,c=b%1000000009,c%1000000009,(a+c)%1000000009
    print(c)