def square_root_bisection(number, tolerance = 0.001, max_iterations = 10):
    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    elif number in [0, 1]:
        print(f'The square root of {number} is {number}')
        return number
    else:
        calculated_root = 0
        iterations = 0

        # By Definition of the Problem: Tolerance is the Difference of the Actual Root to the Calculated Root
        # Therefore: Upper and Lower Bounds for Checking the solution would be the sum and diff of actual and tolerance
        actual_root = number ** 0.5
        upper_bound = actual_root + tolerance
        lower_bound = actual_root - tolerance

        # Consider Different Endpoints for Positive Integers and Values between 0 and 1
        if 0 < number < 1:
            start, end = number, 1
        else:
            start, end = 0, number

        while start <= end and iterations <= max_iterations:
            mid = (start + end) / 2
            
            if upper_bound > mid > lower_bound:
                calculated_root = mid
                print(f'The square root of {number} is approximately {calculated_root}')
                return calculated_root
            if mid > actual_root:
                end = mid 
            else:    
                start = mid 
                
            iterations += 1
        else:
            print(f'Failed to converge within {max_iterations} iterations')
            return None
            
    

square_root_bisection(0.001, 1e-7, 50)

