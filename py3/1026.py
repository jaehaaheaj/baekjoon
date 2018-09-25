n = int(input())
a = sorted([int(i) for i in input().split()])
b = sorted([int(i) for i in input().split()])
b.reverse()
sum = 0
for i in range(n):
    sum+=a[i]*b[i]
print(sum)