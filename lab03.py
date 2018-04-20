def gcd(a, b):
	"""Returns the greatest common divisor of a and b.
	Should be implemented using recursion"""
	if a == b:
		return a
	if a == 1 or b == 1:
		return 1
	elif a == 0 or b == 0:
		return 0
	elif a == 2 or b == 2:
		return 2
	elif a % b == 0:
		return b
	elif b % a == 0:
		return a
	else:
		if a * 2 == b:
			return a
		elif b * 2 == a:
			return b
		else:
			if a < b:
				return gcd(a, b % a)
			elif b < a:
				return gcd(b, a % b)

def hailstone(n):
	""" Print out the hailstone sequence starting at n, and return
	the number of elements in the sequence."""

	if n == 1:
		return 1
	else:
		

