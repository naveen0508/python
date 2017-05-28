# -*- coding: utf-8 -*-
"""
Created on Sun May 14 23:25:56 2017

@author: Naveen

GCD program without lists and scanning backwards
"""

def gcd(m,n):
    
    i = min(m,n)
    
    while i > 0:
        if (m%i) == 0 and (n%i) == 0:
            return(i)
        else:
            i -= 1

print(gcd(14,63))
