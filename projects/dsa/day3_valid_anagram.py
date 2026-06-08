# Day 3 - LeetCode #242: Valid Anagram
# Approach: HashMap | Time: O(n) | Space: O(n)

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        count[char] = count.get(char, 0) - 1
        if count[char] < 0:
            return False

    return True

# Test
print(isAnagram("anagram", "nagaram"))  # True
print(isAnagram("rat", "car"))          # False
print(isAnagram("listen", "silent"))    # True