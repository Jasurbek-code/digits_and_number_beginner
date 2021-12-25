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
    x2 = num // 10 % 10
    x3 = num // 100 % 10
    x4 = num // 1000 % 10
    lens = x1/x1 + x2/x2 + x3/x3 + x4/x4

    return int(lens)

print(get_length(1234))



