for i in range(int(input())):
	s = [int(j) for j in input().split()][1:]
	avrg = sum(s)/len(s)
	print("{0:.3f}".format(round(sum([j>avrg for j in s])/len(s)*100, 3)) + '%')