#get number of digits in an int?
def get_length(num):
    """
    Get length of integer
    
    Args:
        num (int): integer to get length of

    Returns:
        int: length of integer
    """
    # return number of digits in integer

    x1 = num % 10
    num //= 10

    x2 = num % 10
    num //= 10

    x3 = num % 10
    num //= 10

    x4 = num % 10
    num //= 10

    x5 = num % 10

    return  int((x1**0) + (x2**0) + (x3**0) + (x4**0) + (x5**0))

print(get_length(12346))



