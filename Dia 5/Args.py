def suma(*args):
    """
    Returns the sum of the arguments.

    Args:
        *args (int): The numbers to sum.

    Returns:
        int: The sum of the arguments.


    """
    '''total = 0
    for i in args:
        total += i
    return total'''
    sum(args)
    return sum(args)

print(suma(1, 2, 3, 4, 5))