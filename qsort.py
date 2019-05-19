import random
a = [3, 4, 5, 3, 2, 1, 0]

def qsort(a, f = 0, l = len(a)-1):
    if f<l:
        pivot = l
        le=f
        re=f
        while re < l:
            if a[re] <= a[pivot] and re!=pivot:
                if le == pivot:
                    le+=1
                a[le],a[re] = a[re],a[le]
                le+=1
            re+=1
        a[le],a[pivot] = a[pivot],a[le]    
            
        qsort(a, f, le-1)
        qsort(a, le, l)
        return a

qsort(a)
print(a)