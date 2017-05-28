# -*- coding: utf-8 -*-
"""
Created on Mon May 15 22:23:23 2017

@author: Naveen

GCD program according to Euclid's algorithm
"""

def gcd(m,n):
    
    #assume m >= n
    
    if m < n:
        (m,n)=(n,m)
    
    if (m%n) == 0:
        return(n)
    else:
        diff = m-n
        # diff > n ? Possible!
        return(gcd(max(n,diff), min(n,diff)))
    

print(gcd(14,63))