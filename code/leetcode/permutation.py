"""Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2."""


def checkInclusion(s1: str, s2: str) -> bool:
    """time exceeded """
    substring = dict()
    compareDict = dict()
    if len(s2) < len(s1):
        return False
    for char in s1:
        substring[char] = substring.get(char, 0) + 1
    p1 = 0
    p2 = 0
    windowSize = len(s1)
    while p1 < len(s2) and (p2 + windowSize) <= len(s2):
        p2 = p1
        compareDict = substring.copy()
        while p2 < (p2 + windowSize):
            value = compareDict.get(s2[p2], "noKey")
            if value == "noKey":
                p1 = p2 + 1
                break
            elif value == 0:
                p1 += 1
                p2 = p1
                break
            compareDict[s2[p2]] = compareDict.get(s2[p2], 0) - 1
            p2 += 1
            if not any(compareDict.values()):
                return True
    return False


s1 = "adc"
s2 = "dcda"
print(checkInclusion(s1, s2))
s1 = "hello"
s2 = "ooolleoooleh"
print(checkInclusion(s1, s2))
