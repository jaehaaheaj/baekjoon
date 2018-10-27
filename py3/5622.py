def c2t(c):
	n = ord(c)
	adj = ord('A')
	if n>=ord('S'):
		adj+=1
	if n==ord('Z'):
		adj+=1
	n -= adj
	return n//3 + 3

s = input()
print(sum([c2t(i) for i in s]))