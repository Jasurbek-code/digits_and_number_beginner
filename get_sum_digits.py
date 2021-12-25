#Find the sum of digits in an integer
def get_sum_digits(num):
    """
    Get sum of digits in integer
    
    Args:
        num (int): integer to get sum of digits of
    
    Returns:
        int: sum of digits in integer
    """
    # return sum of digits in integer
    x1,x2,x3,x4 = 0,0,0,0

    x1 = num % 10
    num //= 10

    x2 = num % 10
    num //= 10

    x3 = num % 10
    num //= 10

    x4 = num % 10
    num //= 10

    Sum = x1+x2+x3+x4
    return  Sum
print(get_sum_digits(1234))