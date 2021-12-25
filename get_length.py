#get number of digits in an int?
import math
def get_length(num):
    x1, x2, x3, x4 = 0, 0, 0, 0
    """
    Get length of integer
    
    Args:
        num (int): integer to get length of

    Returns:
        int: length of integer
    """
    # return number of digits in integer
    x1 = num % 10
    x2 = num // 10 % 10
    x3 = num // 100 % 10
    len = x1/x1 + x2/x2 + x3/x3

    return int(len)

print(get_length(145))



