for i in range(int(input())):
    eng = {}
    for _ in range(int(input())):
        eng[input()] = True
    res = 0
    found = len(eng)
    for _ in range(int(input())):
        query = input()
        if(eng.get(query)):
            eng[query] = False
            found -= 1
            if(found == 0):
                found = len(eng) - 1
                res += 1
                for key in eng.keys():
                    eng[key] = True
                eng[query] = False
    print("Case #%d: %d" % (i+1, res))