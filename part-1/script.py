import re 

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
    
def f4(a_list1, a_list2, an_int):
    """
    The function should return how many elements from a_list2 appear at least n times in a_list1.
    >>> f4([1, 1, 2, 2, 2, 3, 3, 3, 3], [1, 2], 3)
    1
    >>> f4([1, 1, 1, 2, 2, 2, 3, 3, 3], [1, 2, 3, 4], 4) 
    0
    """
    answer = 0
    for i in a_list2:
        count = 0
        for j in a_list1:
            if i == j:
                count = count+1
        if count >= an_int:
            answer = answer + 1
    return answer

def f5(a_list):
    """
    Returns all slices of a_list
    >>> f5([1, 2, 3])
    [[1], [1, 2], [1, 2, 3]]
    >>> f5([0, 0])
    [[0], [0, 0]]
    >>> f5([])
    []
    """
    new_list = []
    for i in range(1, len(a_list) + 1):
        new_list.append(a_list[:i])
    return new_list

# def f6(a_char):
# # Issue interpreting \t character. So I want 
# # Note: I think this is a mistake - we don't want  
#     """
#     Find all non-alphanumeric characters in the input_string
#     >>> f6('B -34;aJK+]\t>')
#     ' -;+]\t>'
#     >>> f6('python')
#     ''
#     >>> f6('\t')
#     '\t'
#     """
#     return ''.join([char for char in a_char if not char.isalnum()])

def f7(a_str):
    '''
    >>> f7('de het de een')
    '{'de': 2, 'het': 1, 'een':1}
    >>> f7('')
    '{}'
    '''

def f8(a_str):
    '''
    >>> f8('8\n8.2\n4.3\n9.5')
    7.5
    >>> f8('7.5\nNS\n7\n3.5\nNVD')
    6.0
    '''

if __name__ == '__main__':
    import doctest
    doctest.testmod()

