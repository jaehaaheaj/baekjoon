n = int(input())
arr = [[0, 0] for i in range(n)]
step = []
for i in range(n):
	step.append(int(input()))

arr[0] = [step[0], 0]
arr[1] = [arr[0][0]+step[1], step[1]]
for i in range(2, n):
	arr[i] = [arr[i-1][1]+step[i], max(arr[i-2])+step[i]]

print(max(arr[n-1]))