def checker(l):
	if(len(l)==1):
		return True
	c = l[0] - l[1]
	for i in range(len(l)-1):
		if(l[i] - l[i+1] != c):
			return False
	return True

cnt = 0
for i in range(1, int(input()) + 1):
	if(checker([int(c) for c in str(i)])):
		cnt+=1
print(cnt)