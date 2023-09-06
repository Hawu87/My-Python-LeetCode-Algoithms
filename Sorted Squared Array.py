def sortedSquaredArray(array):
    l, r = 0, len(array) - 1
    i = r
    output = [0] * len(array)
    while l <= r:
        #compare the start and end
        if abs(array[l]) > abs(array[r]):
            output[i] = array[l] * array[l]
            l += 1
        else:
            output[i] = array[r] * array[r]
            r -= 1
        i -= 1
    return output
