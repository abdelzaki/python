"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:
Input: strs = ["eat","tea","tan","ate","natt","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
from collections import defaultdict
def groupAnaram(input:list[str]) -> list[list[str]]:
    items = defaultdict(list)
    for word in input:
        temp = {}
        for char in word:
            temp[char] = temp.get(char,0) + 1
        tempstring=""
        for key in sorted(temp):
            tempstring+= str(key) + str(temp[key])
        items[tempstring].append(word)
    print(items)
    return items
#strs = ["eat","tea","tan","ate","natt","bat"]
strs = ["","","","b"]
groupAnaram(strs)


