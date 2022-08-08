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

def checkInclusionFaster(s1: str, s2: str) -> bool:
    l: int = 0
    if not s1:
        return True
    if len(s1) > len(s2):
        return False
    s1Dict: dict[str, int] = dict()
    s2Dict: dict[str, int] = dict()

    for r in range(len(s1)):
        s1Dict[s1[r]] = s1Dict.get(s1[r], 0) + 1
        s2Dict[s2[r]] = s2Dict.get(s2[r], 0) + 1

    for r in range(len(s1), len(s2)):
        if s1Dict == s2Dict:
            return True
        s2Dict[s2[l]] -= 1
        if not s2Dict[s2[l]]:
            del s2Dict[s2[l]]
        l += 1
        s2Dict[s2[r]] = s2Dict.get(s2[r], 0) + 1
    if s1Dict == s2Dict:
        return True
    return False

s1 = "adc"
s2 = "dcda"
print(checkInclusion(s1, s2))
s1 = "hello"
s2 = "ooolleoooleh"
print(checkInclusion(s1, s2))
