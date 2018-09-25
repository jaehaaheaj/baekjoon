s = []
n = int(input())
for i in range(n, 0, -1):
    s += ['*']*(i) + ['\n']
print(''.join(i for i in s))