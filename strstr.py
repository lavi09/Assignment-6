# -*- coding: utf-8 -*-
"""
Created on Fri May 17 23:09:16 2019

@author: Lavi
"""
def strStr(haystack, needle):
       
        i = 0
        while i <= len(haystack) - len(needle):
            if haystack[i:i+len(needle)] == needle:
                return i
            i += 1
        return -1
        



           
s1="Miracles do happen"
s2="happen"
print(strStr(s1,s2))