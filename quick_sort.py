def quicksort(a):
    j=-1
    i=-1
    key=a[i]
    for step in a:
        j+=1
        while (step >= key) and (j<len(a)+i-1):
            i-=1
            save=a[i]
            a[i]=key
            a[i+1]=step
            a[j]=save
            key=a[i]
            step=a[j]
        if (step >= key) :
            a[j]=key
            a[j+1]=step
            break
        elif j==len(a)+i-1:
            break
    if len(a[0:j+1])>=2:
        a[0:j+1]=quicksort(a[0:j+1])
    if len(a[j+1:])>=2:
        a[j+1:]=quicksort(a[j+1:])
    return a    
