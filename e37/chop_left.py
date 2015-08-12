def chop_left(n, prime_list):
    tmp = 10
    while n % tmp != n:
    	if prime_check(n % tmp, prime_list):
    		tmp *= 10
    	else:
    		return False
    return True
