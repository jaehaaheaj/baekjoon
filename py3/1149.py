res = [0,0,0]
for i in range(int(input())):
	c = [int(j) for j in input().split()]
	res = [min(res[1], res[2])+c[0], min(res[2], res[0])+c[1], min(res[0], res[1])+c[2]]
print(min(res))