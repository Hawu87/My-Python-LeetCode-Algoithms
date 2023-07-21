def ThreeSum(A):
	"""Return the indices of three numbers in array A such that their sum is equal 0.
	>>> ThreeSum([-3, -1, 1, 0, 2, 10, -2, 8])
	[[-3, 1, 2], [-2, 0, 2], [-1, 0, 1]]
	>>> ThreeSum([-5, 3, 2, 0, 1, -1, -5, 3, 2])
	[[-5, 2, 3], [-1, 0, 1]]
	"""
	A.sort()
	my_dict = []
	secondToLast = len(A) - 2
	i = 0
	while i < secondToLast:
		findTwoSum(i, A, my_dict)
		i += 1
	return my_dict

def findTwoSum(root, A, my_dict):
	left = root + 1
	right = len(A) - 1
	while left < right:
		sum = A[root] + A[left] + A[right]
		if sum == 0:
			my_dict.append([root, left, right])
		elif sum > 0:
			right -= 1
		else:
			left += 1


