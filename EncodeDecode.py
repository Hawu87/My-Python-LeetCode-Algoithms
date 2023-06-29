class Solution:
	"""
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
	def encode(self, strs):
		res = ""
		for i in strs:
			res += str(len(i)) + "#" + i
		return res

	"""
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
	def decode(self, strs):
		i, output = 0, []
		while i < len(strs):
			j = i + 1
			length = int(strs[i])
			output.append(strs[j + 1: j + 1 + length])
			i = j + 1 + length
		return output
