def count_stair_ways(n):
	if n == 1:
		return 1
	elif n == 0:
		return 0
	elif n == 2:
		return 2
	else:
		return count_stair_ways(n-1) + count_stair_ways(n-2)

def count_k(n, k):
	if n == 0:
		return 1
	elif n < 0:
		return 0
	elif k == 0:
		return 0
	else:
		with_k = count_k(n-k, k)
		without_k = count_k(n, k-1)
		return with_k + without_k
