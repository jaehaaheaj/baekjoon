def dduupp(s):
	cnt, string = int(s[0]), s[1]
	l = [0] * cnt * len(string)
	for i in range(len(string)):
		for j in range(cnt):
			l[i*cnt+j] = str(string[i])
	print(''.join(l))

for i in range(int(input())):
	dduupp(input().split())