def swirlNum(x, y):
	if(x==y and x>=0):
		return ((2*x+1)**2)
	if(abs(x) >= abs(y)):
		if(x >= 0):
			return (2*x-1)**2 + (x-y)
		else:
			return (-2*x-1)**2 - (4*x) + (-(x-y))
	else:
		if(y >= 0):
			return (2*y-1)**2 + 6*y + (x+y)
		else:
			return (-2*y-1)**2 - (2*y) + -(x+y)

def maxLenGen(s):
	l = [swirlNum(s[1], s[0]), swirlNum(s[3], s[0]), swirlNum(s[1], s[2]), swirlNum(s[3], s[2])]
	return max([len(str(x)) for x in l])

s = [int(i) for i in input().split()]
maxLen = maxLenGen(s)
arr = []
for i in range(s[0], s[2]+1):
	row = []
	for j in range(s[1], s[3]+1):
		row.append(str(swirlNum(j, i)).rjust(maxLen))
	arr.append(row)

for i in range(len(arr)):
	print(' '.join(arr[i]))