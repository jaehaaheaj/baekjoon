h = []
for i in range(9):
	h.append(int(input()))
h.sort()
r = sum(h) - 100

for i in range(9):
	end = False
	for j in range(i):
		if(h[i] + h[j] == r):
			h.pop(i)
			h.pop(j)
			for hh in h:
				print(hh)
			end = True
			break
	if(end):
		break