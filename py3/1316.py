def groupChecker(s):
	l = [s[0]]
	for i in range(1, len(s)):
		if(s[i] != s[i-1]):
			if(s[i] in l):
				return False
			l.append(s[i])
	return True

result = 0
for i in range(int(input())):
	if(groupChecker(input())):
		result+=1
print(result)