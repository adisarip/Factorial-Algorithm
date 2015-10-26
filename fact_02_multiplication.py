

def calculate_factorial_multi(number):
	'''
	This function takes one agruments and
	returns the factorials of that number
	

	This function uses the approach successive multiplication

	like 8! = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
	'''
	
	'''
	If 0 or 1 retrun immediately
	''' 
	if number == 1 or number == 0:
		return 1
	
	result = 1 # variable to hold the result
	
	for x in xrange(1, number + 1, 1):
		result *= x
	return result
