"""
LeetCode 20: Valid Parentheses
Pattern: Stack (new pattern family)
Mock Interview #2 - Day 41 (Aug 23, verified fresh problem)

Given a string containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

Valid means:
1. Open brackets must be closed by the same type of bracket.
2. Open brackets must be closed in the correct order.
"""

def isValid(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in "({[":
            stack.append(char)
        else:
            if not stack:
                return False
            if pairs[char] == stack[-1]:
                stack.pop()
            else:
                return False

    return not stack


# Test cases
print(isValid("()[]{}"))   # True
print(isValid("(]"))        # False
print(isValid("([)]"))      # False
print(isValid("{[]}"))      # True
print(isValid(")"))         # False - empty stack on close bracket
print(isValid("((("))       # False - leftover unmatched opens