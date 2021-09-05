def minimumBribes(q):
    # Write your code here
    #   [1, 2, 3, 4, 5]
    #   [2, 1, 5, 3, 4]
    total = 0
    p1 = 1
    p2 = 2
    p3 = 3

    for i in range(len(q)):
        if q[i] == p1:
            p1 = p2
            p2 = p3
            p3 = p3 + 1
        elif q[i] == p2:
            # 3 4
            p2 = p3
            p3 = p3 + 1
            total = total + 1
        elif q[i] == p3:
            total = total + 2
            p3 = p3 + 1
        else:
            print("Too chaotic")
            return

    print(total)

#SCORE = 100