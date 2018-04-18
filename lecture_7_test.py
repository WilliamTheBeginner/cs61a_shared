""" Sum all digits of a number """

""" 2018"""


def sum_digits(n):

	if n < 10:
	
		return n

	else:
	
		first_but_last, last = n // 10, n % 10

		return sum_digits(first_but_last) + last

def sum_digits_using_while(n):

	k = 0

	while n > 10:
		n, last = n // 10, n % 10

		print('N = ', n, 'Last = ', last)

		k = k + last

	k = n + k

	return k 
