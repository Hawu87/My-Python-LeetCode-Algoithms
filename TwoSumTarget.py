def TwoSum(A, target):
    my_dict = {}
    for i, val in enumerate(A):
        if val in my_dict:
            return [my_dict[val], i]
        my_dict[target-val] = i
    return []