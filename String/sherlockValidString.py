def isValid(s):

    a_dic = {}
    a_list = []

    for char in s:
        if char not in a_dic.keys():
            a_dic[char] = 1
        else:
            a_dic[char] = a_dic[char] + 1

    for item in a_dic.values():
        a_list.append(item)

    num = a_list[0]
    counter = 0
    print(a_list)
    for i in range(len(a_list)):

        if num == a_list[i]:
            pass
        elif abs(num - a_list[i]) < 2 or a_list[i] == 1:
            counter = counter + 1
        else:
            return "NO"

        if counter > 1:
            return "NO"

    return "YES"


print(isValid("aaaaabc"))

# SCORE = 100