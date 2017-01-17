def prime_num_gen(n):
    """
    This function takes a given number n as an argument
    and generates prime numbers ranging from zero to n
    Prime Numbers: A number with only two factors - one and itself
    """
    
    if n < 0:
        return None
    elif n == 2:
        return [2]
    elif n ==1 or n == 0:
        return []    
        
    try:
        prime_nums = [2] # initialize with 2 since n is greater than 2 thus far
        for i in range(3,n+1):
            # start from 3 onwards
            # "outer loop"
            factor_count=0
            for x in range (2,i):
                # start from 2 onwards
                if i % x == 0:
                    factor_count+=1
                    # inner loop breaking..
                    break # i is not a prime number 
            if factor_count==0:
                prime_nums.append(i)
    except TypeError as e:
        # n is not an integer
        raise(e)
    return prime_nums
    
# print(prime_num_gen(20))
        
        
        
