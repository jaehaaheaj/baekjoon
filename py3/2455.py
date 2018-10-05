now, best = 0, 0
for i in range(4):
	s = [int(i) for i in input().split()]
	now += s[1] - s[0]
	best = min(now, 10000) if now>best else best
print(best)