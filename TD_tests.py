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