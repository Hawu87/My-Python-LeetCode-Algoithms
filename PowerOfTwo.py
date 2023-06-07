def power(n):
	"""Return True if n is a power of 2
	>>> power(2)
	True
	>>> power(16)
	True
	>>> power(12)
	False
	>>> power(-1)
	False
	>>> power(524288)
	True
	"""
	#Brute force migh be to divide the number repeatedly by 2 to check if it gets to one
	return (n > 0) and (n & (n - 1)) == 0
	#convert n to bits, and if n is a power of two, if you check it against n - 1 it should give you zero
