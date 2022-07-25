"""Given a string s, find the length of the longest substring without repeating characters."""


def lengthOfLongestSubstring(s: str):

    uniqueSet = list()
    uniqueSet = list()
    length, maxlength = 0, 0
    for char in s:
        if char not in uniqueSet:
            uniqueSet.append(char)
            length += 1
            maxlength = max(maxlength, length)
        else:
            uniqueSet.append(char)
            index = uniqueSet.index(char)
            uniqueSet = uniqueSet[index+1:]
            length -= (index)
            maxlength = max(maxlength, length)
    return maxlength



s = "abcabcbb"
print(lengthOfLongestSubstring(s))
