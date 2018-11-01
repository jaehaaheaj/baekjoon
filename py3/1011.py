for n in range(int(input())):
	s = input().split()
	dist = int(s[1]) - int(s[0])
	i = int(-(-(pow(dist+1/4, 1/2)-0.5)//1)) - 1
	extra = 2 if dist - i*(i+1) > i + 1 else 1
	print(2 * i + extra)