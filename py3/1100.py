cnt = 0
for i in range(8):
	cnt += sum([f=='F' for f in input()[i%2::2]])
print(cnt)