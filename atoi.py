# -*- coding: utf-8 -*-
"""
Created on Fri May 17 22:41:50 2019

@author: Lavi
"""
def IsNumeric(x):
    if(x>='0' and x<='9'):
        return True
    return False
    
def atoi(s):
    res=0
    sign=1
    i=0
    if s[0]=='-':
        sign=-1
        i+=1
    for j in range(i,len(s),1):
        if IsNumeric(s[j])==False:
            return 0
        res=res*10+ord(s[j])-ord('0') 
    return sign*res
    





s="10"
print(atoi(s))