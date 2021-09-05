def substrCount(n, s):
    counter = 0
    for i in range(n):
        counter = counter + 1
        for j in range(i+1,n):
            if s[i] != s[j]:
                if s[i:j] == s[j+1:2*j-i+1]:

            else:
                counter = counter + 1


    return counter


print(substrCount(8, "mnonopoo"))
# print(substrCount(3, "asd"))



# def substrCount(n, s):
#     counter = 0
#     for i in range(n+1):
#         for j in range(i):
#             sub = s[j:i]
#             print(sub)
#
#     return counter

