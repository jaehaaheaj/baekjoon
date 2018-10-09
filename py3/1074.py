s = [int(i) for i in input().split()]
n = s[0]
r, c = bin(s[1])[2:].zfill(n), bin(s[2])[2:].zfill(n)
print(sum([(2*int(r[i]) + int(c[i])) * 2**(2*(n-i-1)) for i in range(n)]))