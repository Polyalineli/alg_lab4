import numpy as np

def selection_sort(a):
    l=len(a)
    s= []
    while len(s)<l:    
        index_min=0
        mini = a[index_min]    
        for i in range(len(a)):
            if a[i] <= mini:
                index_min = i
                mini=a[index_min]
        s.append(mini)
        a = np.delete(a, index_min)
    return s

