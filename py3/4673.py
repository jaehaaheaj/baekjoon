limit = 10000
arr = [True]*(limit+1)
arr[0] = False

def genSelfNum(i):
	while(1):
		i += sum([int(j) for j in str(i)])
		if(i>limit):
			break
		arr[i] = False

for i in range(limit):
	if(arr[i]):
		genSelfNum(i)

for i in range(limit+1):
	if(arr[i]):
		print(i)