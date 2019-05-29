def quicksort(a):
    if a==[]:
        return a

    first = a[0]
    lesser = quicksort([x for x in a[1:] if x < first])
    greater = quicksort([x for x in a[1:] if x >= first])

    return lesser + [first] + greater
    
