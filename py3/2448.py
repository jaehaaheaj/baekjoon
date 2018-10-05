def getPower(x):
	x/=3
	cnt = 0
	while(x!=1):
		x/=2
		cnt+=1
	return cnt

def genPattern(i):
	o = i+i
	for x in range(len(i)*2):
		o[x] += ' '*len(i[x%len(i)]) if x<len(i) else i[x%len(i)]
	return o

n = 24

unit = ['*     ','* *   ','***** ']
for i in range(getPower(n)):
	unit = genPattern(unit)

for i in range(len(unit)):
	print((' '*(len(unit)-i) + unit[i])[1:len(unit[-1])])