# -*- coding: utf-8 -*-
"""
Created on Sun May 14 12:00:53 2017

@author: Naveen

Greatest Common Divisor program
"""
def gcp(m,n):
    fm = []
    for i in range(1, m+1):
        if (m%i) == 0:
            fm.append(i)
    
    fn = []
    for j in range(1, n+1):
        if (n%j) == 0:
            fn.append(j)
    
    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)
    
    return(cf[-1])


print(gcp(14,63))