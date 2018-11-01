s = input()
l = [0]*10
for i in range(len(s)):
	l[int(s[i])] += 1
l[6] = int((l[6] + l[9] + 1) / 2)
l[9] = 0
print(max(l))