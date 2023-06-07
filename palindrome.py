from math import log

def isPalindrome(x):
	"""Return True if a number is a palindrome, and False if otherwise
	>>> isPalindrome(1)
	True
	>>> isPalindrome(123)
	False
	>>> isPalindrome(-1)
	False
	>>> isPalindrome(12321)
	True
	"""
	if x < 0:
		return False
	total_dig = int(log(x, 10)) + 1
	mask, i = pow(10, total_dig - 1), 0
	while i < total_dig // 2:
		msd = x // mask
		lsd = x % 10
		if msd != lsd:
			return False
		x %= mask
		x //= 10
		mask /= 100
		i += 1
	return True
