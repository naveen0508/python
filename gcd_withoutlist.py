# -*- coding: utf-8 -*-
"""
Created on Sun May 14 23:09:35 2017

@author: Naveen

GCD program with creating list
"""

def gcd(m,n):
    
    for i in range(1, min(m,n)+1):
        if (m%i) == 0 and (n%i) == 0:
            mrcf = i
    return(mrcf)

print(gcd(14,63))