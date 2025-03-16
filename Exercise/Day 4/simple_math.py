def add(a, b):
    """ 
    Add two numbers.
    
    Parameters
    ----------
    a : float
        First number.
    b : float
        Second number.

    Returns
    -------
    float
        Sum of a and b.
    """
    return a + b

def subtract(a, b):
    """ 
    Subtract two numbers.
    
    Parameters
    ----------
    a : float
        First number.
    b : float
        Second number.

    Returns
    -------
    float
        Difference of a and b.
    """
    return a - b

def multiply(a, b):
    """ 
    Multiply two numbers.
    
    Parameters
    ----------
    a : float
        First number.
    b : float
        Second number.

    Returns
    -------
    float
        Product of a and b.
    """
    return a * b

def divide(a, b):
    """ 
    Divide two numbers.
    
    Parameters
    ----------
    a : float
        First number.
    b : float
        Second number.

    Returns
    -------
    float
        Quotient of a and b.

    Raises
    ------
    ZeroDivisionError
        If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b