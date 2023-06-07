def TwoSum(n):
	"""Return a list of index tuple pair is their sum is zero
	>>> TwoSum([1,2,3,4])
	[]
	>>> TwoSum([1,-1, 2, 0,-2])
	[(0, 1), (1, 0), (2, 4), (4, 2)]
	"""
	my_dict = {}
	for i, val in enumerate(n):
		my_dict[val] = i
	array = []
	for i, val in enumerate(n):
		if -val in my_dict:
			if i != my_dict[-val]:
				array.append((i, my_dict[-val]))
	return array