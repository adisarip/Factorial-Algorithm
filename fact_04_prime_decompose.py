
def calculate_factorial_prime_decompose(number):
    '''
    This function takes one integer 
    agruments and return the factorial of the agruments.

    Since there are (number / ln number) prime number smaller than number
    so we can further reduce the total number of multiplication

    '''
    prime = [True]*(number + 1)
    result = 1
    for i in xrange (2, number+1):
        if prime[i]:
            #update prime table
            j = i+i
            while j <= number:
                prime[j] = False
                j += i
            #calculate number of i in n!
            sum = 0
            t = i
            while t <= number:
                sum += number/t
                t *= i
            result *= i**sum
    return result
    
    
