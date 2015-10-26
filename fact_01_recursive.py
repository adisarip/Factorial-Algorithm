

def calculate_factorial_recursive(number):
	'''
	This function takes one agruments and
	returns the factorials of that number
	This is naive recursive approach
	'''
	#base case
	if number == 1 or number == 0:
		return 1
	return number * calculate_factorial_recursive(number - 1)
