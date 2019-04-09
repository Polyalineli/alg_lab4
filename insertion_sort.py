#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

def insertion_sort(a):
    if len(a)>0:    
        s = np.array([a[0]])
        for i in range(1, len(a)):  
            for j in range(len(s)):
                if a[i] <= s[j]:
                    if j==0:
                        s = np.insert(s, 0, [a[i]])
                        break                
                    elif a[i] >= s[j-1]:
                        s = np.insert(s, j, [a[i]])
                        break                                   
                elif a[i] > s[j]:
                    l = len(s)-1
                    if 0>j>l and a[i] <= s[j-1]:
                        s = np.insert(s, j+1, [a[i]])
                        break
                    elif j== l:
                        s = np.insert(s, l+1, [a[i]])
                        break
        return s
    else:
        return np.array(a)
#b =np.array([2, 1, 0, -1, -2])
#print(insertion_sort(b))