def characterReplacement(s: str, k: int) -> int:
    l, r = 0, 0
    charDict = dict()
    maxNumber = 0
    for char in s:
        r += 1
        charDict[char] = charDict.get(char, 0) + 1
        maxNumber = max(maxNumber, charDict.get(char))
        if (r - l + 1) - maxNumber > k:
            charDict[char] -= 1
            l += 1
        maxLength = max(maxNumber,r-l +1)
    return maxLength

s = "ABAB"
k = 2
print(characterReplacement(s,k))
