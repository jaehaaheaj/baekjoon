def numGen(x):
	a,b = int(x/10),x%10
	return 10*b + (a+b)%10

init = int(input())
x = init
cnt = 0
while(1):
	cnt += 1
	x = numGen(x)
	if(x==init):
		break
print(cnt)