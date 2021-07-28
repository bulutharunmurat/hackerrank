def substrCount(n, s):
    counter = 0
    for i in range(n+1):
        for j in range(i):
            sub = s[j:i]
            print(sub)


    return counter

# print(substrCount(8, "mnonopoo"))
print(substrCount(3, "asd"))


