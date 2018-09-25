def dist(x1, y1, x2, y2):
	return ((x1-x2)**2 + (y1-y2)**2)**0.5

def routeChecker(x1, y1, x2, y2, p1, p2, r):
	return (dist(x1, y1, p1, p2) < r) ^ (dist(x2, y2, p1, p2) < r)

for i in range(int(input())):
	coord = input().split()
	x1, y1, x2, y2 = int(coord[0]), int(coord[1]), int(coord[2]), int(coord[3])
	cnt = 0
	for j in range(int(input())):
		p = input().split()
		cnt = cnt + int(routeChecker(x1, y1, x2, y2, int(p[0]), int(p[1]), int(p[2])))
	print(cnt)

