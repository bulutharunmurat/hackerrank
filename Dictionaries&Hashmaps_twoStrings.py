def twoStrings(s1, s2):
    flag = False
    a = {}
    b = {}
    for element in s1:
        if element not in a.keys():
            a[element] = 0
        a[element] += 1
    for element in s2:
        if element not in b.keys():
            b[element] = 0
        b[element] += 1

    for key in a.keys():
        if key in b.keys():
            flag = True
            break
        else:
            pass
    if flag == True:
        return "YES"
    else:
        return "NO"

#SCORE = 100