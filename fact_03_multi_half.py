
def calculate_factorial_multi_half(number):
	
	'''

	This function takes one agruments and
	returns the factorials of that number

	This function make use of the fact that we can reduce the multiplication in factorial
	by half, for even number
	
	Multiplication is an expensive operation so replacing multplication with addition 
	we are reduction the strength.Strength Reduction is a Process most often used
	by the compiler.

	Lets calculate 8!

	so 8! = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 -	let group them together:

	8! = (8 * 1) * (7 * 2) * (6 * 3) * (5 * 4)

	Which can be written as

	8! = 8 * (8 + 6 = 14) * (14 + 4 = 18) * (18 + 2)
		so first factor is the number we are taking. second factor is the first factor 
		plus first factor minus two from the factor
		and then in next we add the result with substarcted result.

	Odd number also follows the same pattern till even just handle the case of one odd
	'''

	'''
	return immediately if number is 0 or 1
	'''
	if number == 1 or number == 0:
		return 1

	handle_odd = False
	upto_number = number
	
	if number & 1 == 1:
		upto_number -= 1
		print upto_number
		handle_odd = True

	next_sum = upto_number
	next_multi = upto_number
	factorial = 1
	
	while next_sum >= 2:
		factorial *= next_multi
		next_sum -= 2
		next_multi += next_sum

	if handle_odd:
		factorial *= number

	return factorial
	
	
	
