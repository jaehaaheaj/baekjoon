n = int(input())
a = [int(i) for i in input().split()]
arr = [[] for i in range(1000+1)]

for i in range(n):
	arr[a[i]].append(i)

order = []
for i in range(len(arr)):
	order += arr[i]

sol = [0]*n
for i in range(len(order)):
	sol[order[i]] = i

print(' '.join([str(i) for i in sol]))