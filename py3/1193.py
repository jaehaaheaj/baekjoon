x = int(input())
i = int(-(-(pow(x*2+1/4, 1/2)-0.5)//1))

n = x - int(i*(i-1)/2)
over, under = i+1-n, n
if i%2 == 0:
	over, under = under, over

print(str(over) + '/' + str(under))