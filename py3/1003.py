fib = [1, 0]
for i in range(40):
	fib.append(fib[-1] + fib[-2])

n = int(input())
for i in range(n):
	x = int(input())
	print(fib[x], fib[x+1])
