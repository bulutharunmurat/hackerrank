def minimumAbsoluteDifference(arr):
    diff = 10**20

    arr = sorted(arr)

    for i in range(len(arr)-1):
        if abs(arr[i] - arr[i+1]) < diff:
            diff = abs(arr[i] - arr[i+1])

    return diff


print(minimumAbsoluteDifference([-2, 2, 4]))


#SCORE = 100


#TIME COMPLEXITY!!! (BELOW CODE)


# def minimumAbsoluteDifference(arr):
#     diff = abs(arr[0]-arr[1])
#
#
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if abs(arr[i] - arr[j]) < diff:
#                 diff = abs(arr[i] - arr[j])
#
#     return diff