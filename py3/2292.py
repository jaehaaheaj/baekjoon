s = int(input())
res, n = 1, 1
while(True):
	if s<=n:
		print(res)
		break
	n += 6*res
	res+=1