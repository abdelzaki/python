""" Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
"""


def isValid(s: str) -> bool:
    stack = list()
    closeToOpen = {")": "(",
                   "]": "[",
                   "}": "{"}
    for shape in s:
        if shape in closeToOpen:
            if stack and closeToOpen[shape] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(shape)
    if not stack:
        return True


s = "()[]{}"
print(isValid(s))
