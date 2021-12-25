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
    x5 = num // 10000 % 10

    uz = x1-(x1-1)+x2-(x2-1)+x3-(x3-1)+x4-(x4-1)+x5-(x5-1)
    return  uz

print(get_length(12346))



