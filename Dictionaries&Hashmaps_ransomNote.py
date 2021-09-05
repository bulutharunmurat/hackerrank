def checkMagazine(magazine, note):
    flag = True
    n = {}
    m = {}
    for element in note:
        if element not in n.keys():
            n[element] = 0
        n[element] += 1
    for element in magazine:
        if element not in m.keys():
            m[element] = 0
        m[element] += 1

    for key in n.keys():
        if key not in m.keys():
            flag = False
            break
        if n[key] > m[key]:
            flag = False
            break
    if flag == True:
        print("Yes")
    else:
        print("No")

#SCORE = 100