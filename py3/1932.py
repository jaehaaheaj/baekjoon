n, res = int(input()), [int(input())]
for i in range(1, n):
	newres = [int(x) for x in input().split()]
	for j in range(len(newres)):
		newres[j] += max(res[max(j-1, 0)], res[min(j, i-1)])
	res = newres
print(max(res))