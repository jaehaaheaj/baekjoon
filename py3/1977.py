m, n = int(input()), int(input())
a = [m] if m in [int(m**0.5)**2, (int(m**0.5)+1)**2] else []
a += [int(i**2) for i in range(int(m**0.5)+1, int(n**0.5)+1)]
if(len(a)==0):
	print(-1)
else:
	print(sum(a))
	print(a[0])