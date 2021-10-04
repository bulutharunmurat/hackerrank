def substrCount(n, s):
    counter = -1
    for i in range(n + 1):
        counter = counter + 1
        for j in range(i):
            sub_string = s[j:i]
            # print(sub_string)
            if len(sub_string) % 2 == 0:
                if len(set(sub_string)) == 1:
                    counter = counter + 1
            else:
                middleelement = int(len(sub_string) / 2)
                sub_string = sub_string[0: middleelement] + sub_string[middleelement+1:]
                print(sub_string)
                if len(set(sub_string)) == 1:
                    counter = counter + 1
    return counter


print(substrCount(8, "mnonopoo"))
# print(substrCount(3, "asd"))

