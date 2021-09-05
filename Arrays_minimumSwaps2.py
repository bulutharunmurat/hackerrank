def minimumSwaps(arr):
    # 1 3 5 2 4 6 7
    '''
    count = 0
    for i in range(len(arr)):
        if not arr[i] == i + 1:
            tem = arr.index(i+1)
            arr[i],arr[tem] = arr[tem], arr[i]
            count = count + 1
    return count
    '''
    count = 0
    for index in range(len(arr)):

        while index + 1 != arr[index]:
            swapIndex = arr[index] - 1  # swapIndex = 2
            valAtIndex = arr[index]  # val = 3
            valAtSwapIndex = arr[swapIndex]  # valswap = 5
            arr[index] = valAtSwapIndex  #
            arr[swapIndex] = valAtIndex
            count += 1
    return count

#SCORE = 100