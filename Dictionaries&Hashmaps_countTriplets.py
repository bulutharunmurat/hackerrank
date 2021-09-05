arr = [1, 2, 2, 4]
r = 2
arr2 = [1, 3, 9, 9, 27, 81]
r2 = 3
arr3 = [1, 5, 5, 25, 125]
r3 = 5

from collections import defaultdict

def countTriplets(lst, ratio):

    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0
    for k in lst:
        count += v3[k]
        v3[k * ratio] += v2[k]
        v2[k * ratio] += 1

    return count


print(countTriplets(arr, r))
print(countTriplets(arr2, r2))
print(countTriplets(arr3, r3))

#SCORE = 100

