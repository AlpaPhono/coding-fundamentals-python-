'''
Module docstring

'''

def count(sequence, item):
    '''
    Counts how many occurances of an item are in an iterable
    Args:
        Sequence (iterable):
        item:

    Returns:
        y (int): number of occurances found
    '''
    y = 0
    for n in sequence:
        if n == item:
            y += 1

    return y
