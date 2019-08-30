def dfs(seqList, order, x):
    for i in seqList[x]:
        dfs(seqList, order, i)
    order.append(x)

def topologicalSort(seqList, target):
    # dfs version
    order = []
    dfs(seqList, order, target)
    return order

def calcTime(finTimeList, seqList, bldgTime, x):
    t = 0
    for i in seqList[x]:
        calcTime(finTimeList, seqList, bldgTime, i)
        t = max(t, finTimeList[i])
    finTimeList[x] += bldgTime[x]

caseNum = int(input())
for cases in range(caseNum):
    s = input().split()
    bldgNum, ruleNum = int(s[0]), int(s[1])
    
    bldgTime = [0] # init
    bldgTime += [int(i) for i in input().split()]

    seqList = [[] for i in range(bldgNum+1)]
    for rules in range(ruleNum):
        rule = input().split()
        seqList[int(rule[1])].append(int(rule[0]))
    finTimeList = [-1 for i in range(bldgNum+1)]
    target = int(input())
    calcTime(finTimeList, seqList, bldgTime, target)
    print(finTimeList[target])