def ContainsDup(A):
    my_dict = set()
    for val in A:
        if val in my_dict:
            return True
        my_dict.add(val)
    return False

