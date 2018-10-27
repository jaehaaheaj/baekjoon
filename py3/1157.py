def mostFreqChar(s):
	cnt = ord('a') - ord('A')
	l = [0]*cnt
	for i in range(len(s)):
		l[(ord(s[i]) - ord('A'))%cnt] += 1
	maxCnt = -1
	result = -1
	multiRes = False
	for i in range(len(l)):
		if(l[i]>maxCnt):
			maxCnt = l[i]
			result = i
			multiRes = False
		elif(l[i]==maxCnt):
			multiRes = True
	return '?' if multiRes else chr(result + ord('A'))

s = input()
print(mostFreqChar(s))