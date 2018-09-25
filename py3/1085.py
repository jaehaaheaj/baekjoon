s = [int(i) for i in input().split()]
print(min(min(s[2] - s[0], s[0]), min(s[3] - s[1], s[1])))