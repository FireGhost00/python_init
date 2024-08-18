def suma(**kwargs):
    """
    Returns the sum of the arguments.

    Args:
        **kwargs (int): The numbers to sum.

    Returns:
        int: The sum of the arguments.


    """
    total = 0
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total


print(suma(a=1, b=2, c=3, d=4, e=5))