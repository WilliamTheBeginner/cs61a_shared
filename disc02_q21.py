def multiply(m, n):
	if n == 1:
		return m
	else: 
		return m + multiply(m, n - 1)

def countdown(n):
	if n == 1:
		print(n)
	else:
		print(n)
		countdown(n-1)

def countup(x, n=0):
	if n == x:
		print(n)
	else:
		print(n)
		countup(x, n=n+1)

def sum_digits(n):
	if n < 10:
		return n
	else:
		all_but_last, last = n // 10, n % 10
		return sum_digits(all_but_last) + last