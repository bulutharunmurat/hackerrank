def luckBalance(k, contests):
    counter = 0
    for i in range(k):

        max = contests[0][0]
        for j in range(len(contests)):
            if contests[j][0] > max and contests[j][1] == 1:
                max = contests[j][0]

        counter = counter + max

        contests.remove([max, 1])


    for element in contests:
        if element[1] == 1:
            counter = counter - element[0]
        else:
            counter = counter + element[0]

    return counter


print(luckBalance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]))
