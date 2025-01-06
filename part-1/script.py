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

def f2(an_int):
    """
    >>> f2(234)
    '00:03:54'
    >>> f2(7322)
    '02:02:02'
    """
    hours = 0
    minutes = 0
    seconds = an_int
    minutes = seconds // 60
    hours = seconds // 3600
    if (minutes):
        seconds = (seconds - minutes*60)
        if (hours):
            minutes = (minutes-hours*60)
    
    return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == '__main__':
    import doctest
    doctest.testmod()


