s = []
n = int(input())
for i in range(n):
    s += [' ']*(n-i-1) + ['*']*(2*i+1) + ['\n']
print(''.join(i for i in s))