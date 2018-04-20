from operator import add, mul
identity = lambda x: x
square = lambda x: x * x
odd = lambda x: x % 2 != 0
greater_than_5 = lambda x: x > 5

def accumulate(combiner, base, n, term):
	""" Return the result of combining the first n terms in a sequence and base. 
	The terms to be combined are term(1), term(2), ..., term(n). combiner is 
	a two-argument communtative function"""

	if n == 0 and base >= 1:
		return base
	elif n == 1 and base == 0:
		return term(n)

	else:
		return combiner(term(n), accumulate(combiner, base, n-1, term)) 

def summation_using_accumulate(n, term):
	""" Returns the sum of term(1) + ... + term(n). The implementation uses
	accumulate."""

	return accumulate(add, 0, n, term)

def product_using_accumulate(n, term):

	return accumulate(mul, 0, n, term)

def filtered_accumulate(combiner, base, pred, n, term):
	"""Return the result of combining the terms in a sequence of N terms
	that satisfy the predicate pred. combiner is a two-argument function.
	If v1, v2, ..., vk are the values in term(1), term(2), ..., term(N)
	that satisfy pred, then the result is
		base combiner v1 combiner v2 ... combiner vk
	(treating combiner as it were a binary operator, like +). The
	implementation uses accumulate. """
	if n == 0 and base >= 1:
		return base
	elif n == 1 and base == 0:
		return term(n)
	if n == 1 and base == 1:
		return n
	if pred(term(n)) == True:
		return combiner(term(n), filtered_accumulate(combiner, base, pred,n-1, term))
	elif pred(base) == True:
		return term(base)
	else:
		return filtered_accumulate(combiner, base, pred, n-1, term)

def make_repeater(term, n):
	""" Return the function that computes the nth application of f. """
	def repeat(x, n=n, term = term):
		if n == 1:
			return term(x)
		elif n == 0:
			return x
		else:
			return term(repeat(x, n-1))

	return repeat

triple = lambda x: x *3

