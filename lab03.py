def gcd(a, b):
	"""Returns the greatest common divisor of a and b.
	Should be implemented using recursion"""
	if a == b / 2:
		return a
	elif b == a / 2:
		return b
	else:
		if a < b:
			return gcd(a, b % a)
		elif b < a:
			return gcd(b, a % b)