for i in range(int(input())):
    s = [int(j) for j in input().split()]
    output = s[0]**(s[1]%4 + 4)%10
    print(10 if output==0 else output)