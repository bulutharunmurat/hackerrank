def sherlockAndAnagrams(s):
    adic = {}
    l = len(s)
    sum = 0
    for i in range(l):
        for j in range(i+1, l+1):
            # print(sorted(s[i:j]))
            # print("".join(sorted(s[i:j])))
            element = "".join(sorted(s[i:j]))
            # print(element)
            if element in adic.keys():
                adic[element] += 1
            else:
                adic[element] = 1
            sum = sum + adic[element] - 1
    return sum

print(sherlockAndAnagrams("ifailuhkqq"))

#SCORE = 100