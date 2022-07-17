import re


def isPalindrome(s: str) -> bool:
    s = s.lower().replace(" ","")
    s =  re.sub(r'[^a-zA-Z0-9]', '',  s )
    print(s)
    indexForward = 0
    indexReverse = len(s) -1
    while(indexReverse > indexForward):
        if s[indexForward] == s[indexReverse]:
            indexForward+=1
            indexReverse-=1
        else:
            return False
    return True

s = "ab_a"
print(isPalindrome(s))