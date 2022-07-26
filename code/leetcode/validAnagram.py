"""Given two strings s and t,
return true if t is an anagram of s, and false otherwise."""

from collections import defaultdict
from operator import truediv


def isAnagram(s: str, t: str) -> bool:
    """solution with sort"""
    # create two dictionary to store the data
    sdict, tdict = defaultdict(str), defaultdict(str)
    if len(s) != len(t):
        return False
    for i in range(len(t)):
        tdict[t[i]] = tdict.get(t[i], 0) + 1  
        sdict[s[i]] = sdict.get(s[i], 0) + 1
        
    if sdict == tdict:
        return True
    return False  

s,t = "anagram", "nagaram"
print(isAnagram(s,t))