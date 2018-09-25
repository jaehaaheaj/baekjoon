s = []
n = int(input())
for i in range(n, 0, -1):
    s += [' ']*(n-i) + ['*']*(2*i-1) + ['\n']
print(''.join(i for i in s))