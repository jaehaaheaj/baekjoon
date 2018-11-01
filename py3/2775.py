for n in range(int(input())):
	f, g = int(input()), int(input()) - 1
	arr = [[i+1 for i in range(g+1)] for j in range(f+1)]
	for i in range(1, f+1):
		for j in range(1, g+1):
			arr[i][j] = arr[i-1][j] + arr[i][j-1]
	print(arr[f][g])