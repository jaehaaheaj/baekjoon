num, res = int(input()), list(input())
cmpind = [i for i in range(len(res))]
for _ in range(num-1):
    new = input()
    for i in reversed(range(len(cmpind))):
        if(res[cmpind[i]] != new[cmpind[i]]):
            res[cmpind[i]] = '?'
            del cmpind[i]
print("".join(res))