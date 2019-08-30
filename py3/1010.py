# sol(x, y) = sum([sol(x-1, y-1), sol(x-1, y-2), ..., sol(x-1, x-1)])
# sol(k, k) = 1
# sol(1, k) = k
# for each testcase, update max y for all 0<i<x

caseNum = int(input())

s = input().split()
x, y = int(s[0]), int(s[1])