#!/opt/homebrew/bin/python3


def f1(an_int):
    """
    >>> f1(1)
    1
    >>> f1(10)
    9
    """
    n=0
    while (3^n<=an_int):
        n = n+1
    return n+1

if __name__ == '__main__':
    import doctest
    doctest.testmod()

def f2(an_int):
    """
    >>>

    """
