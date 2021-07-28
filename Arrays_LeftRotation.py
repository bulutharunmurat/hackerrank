def rotLeft(a, d):
    # Write your code here
    for i in range(d):
        a.append(a.pop(0))
    return a


#SCORE = 100