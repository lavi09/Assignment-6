# -*- coding: utf-8 -*-
"""
Created on Sat May 18 00:33:09 2019

@author: Lavi
"""

def lengthOfLongestSubstring( word):
    # Initially we can go as far to the left as we want
    left_most_valid = 0
    longest = 0
    last_seen = {}

    for i, letter in enumerate(word):
        if letter in last_seen:
            # left_most_valid must be greater than any position which has been seen again
            left_most_valid = max(left_most_valid, last_seen[letter] + 1)
        last_seen[letter] = i

        # Length of substring from left_most_valid to i is i - left_most_valid + 1
        longest = max(longest, i - left_most_valid + 1)

    return longest
word="GEEKSFORGEEKS"
print(lengthOfLongestSubstring(word))