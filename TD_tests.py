#exercice 2
def puissance(x, n):
    """
    >>> puissance(0,5)
    0
    >>> puissance(5,0)
    1
    >>> puissance(2,2)
    4
    """
    r = 1
    for i in range(n):
        r = r * x
    return r

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
    
#exercice 3
def appartient(v,t):
    """
    >>> appartient(4,[])
    False
    >>> appartient(6,[4,5,7])
    False
    >>> appartient(5,[4,5,6])
    True
    """
    for element in t :
        if v == element :
            trouvee = True
        else :
            trouvee = False
    return trouvee

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)

#exercice 4
#1)
#V1
def est_croissant(t):
    """
    >>> est_croissant([9,5,4])
    False
    """
    i = len(t) - 1
    while i >= 0:
        if t[i] <= t[i+1] :
            return True
        else :
            return False
        i = i - 1

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)

#V3
def est_croissant(t):
    """
    >>> est_croissant([1,2,3])
    True
    """
    i = len(t) - 1
    while i >= 0:
        if t[i-1] > t[i] :
            return False
        i = i - 1
    return True
print(est_croissant([1,2,3]))

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)

#V4
def est_croissant(t):
    """
    >>> est_croissant([])
    False
    """
    i = len(t) - 1
    while i > 0:
        if t[i-1] > t[i] :
            return False
        i = i - 1
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)

#2)
#V2
def est_croissant(t):
    """
    >>> est_croissant([9,5,4])
    False
    >>> est_croissant([1,2,3])
    True
    >>> est_croissant([])
    False
    """
    i = len(t) - 1
    while i >= 0:
        if t[i-1] <= t[i] :
            return True
        else :
            return False
        i = i - 1
        
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
