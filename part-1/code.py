#!/opt/homebrew/bin/python3

def f1(an_int):
    """
    Return the greatest power of 3 that is smaller than or equal to an_int
    >>> f1(1)
    1
    >>> f1(10)
    9
    """
    n=0
    while (3 ** n<=an_int):
        n += 1
    return 3 ** (n-1)

def f2(an_int):
    """
    The function should return a string that contains the time in the format hh:mm:ss.
    >>> f2(234)
    '00:03:54'
    >>> f2(7322)
    '02:02:02'
    """
    hours = an_int // 3600 
    minutes = (an_int % 3600) // 60
    seconds = an_int % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def f3(a_list):
    """
    >>> f3([4,5,6])
    (1, 5)
    >>> f3([-3,-5,7])
    (0, -3)
    """
    sorted = list(a_list)
    sorted.sort()
    return (a_list.index(sorted[1]),sorted[1])
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

