for n in range(int(input())):
	s = [int(i) for i in input().split()]
	h, num = s[0], s[2]-1
	print(str(num%h+1) + str(num//h+1).zfill(2))