s = []
for i in range(int(input())):
    s += ['*']*(i+1) + ['\n']
print(''.join(i for i in s))