# -*- coding: utf-8 -*-
"""
Created on Fri May 17 23:49:53 2019

@author: Lavi
"""
def prefixutil(s1,s2):
    n1=len(s1)
    n2=len(s2)
    i=0
    j=0
    result=""
    while(i<=n1-1 and j<=n2-1):
        if(s1[i]!=s2[j]):
            break
        result+=s1[i]
        i,j=i+1,j+1 
    print(result)
    return result
    

def commonprefix(a,low,high):
    if low==high:
        return a[low]
    if high>low:
        mid=low+(high-low)//2
        s1=commonprefix(a,low,mid) 
        print(s1)
        s2=commonprefix(a,mid+1,high)  
        print(s2)
        print(s1,s2)
        return prefixutil(s1,s2)

a=["apple","ape","April"]
n=len(a)
commonprefix(a,0,n-1)
