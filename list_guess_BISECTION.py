def bisect_search1(L, e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len (L)//2
        if L[half] > e:
            return bisect_search1 (L[:half], e)
        else:
            return bisect_search1 (L[half:], e)

L = [1, 2, 3, 4, 5, 6]

print (bisect_search1 (L, 2))