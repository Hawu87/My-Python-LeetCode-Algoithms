from math import sqrt
def isPrime(n):
	"""Return a list of prime numbers less than n
	>>> isPrime(9)
	[2, 3, 5, 7]
	>>> isPrime(2)
	[]
	>>> isPrime(16)
	[2, 3, 5, 7, 11, 13]
	"""
	output = []
	prime_dict = {}
	for i in range(n):
		prime_dict[i] = True
	prime_dict[0] = False
	prime_dict[1] = False
	i = 2
	while i < n:
		if prime_dict[i]:
			j = i + i
			while j < n:
				prime_dict[j] = False
				j += i
			output.append(i)
		i += 1
	return output
