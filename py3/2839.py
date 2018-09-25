n = int(input())
r = -n%5
r = (r + 5 * (r%2)) / 2
if(n-3*r >= 0):
	print(int((n - 3*r)/5 + r))
else:
	print(-1)
