# Day 16: Missing Number, Find Disappeared Numbers, Valid Palindrome

# Problem 1: Missing Number
def missingNumber(nums):
    n = len(nums)
    expected_sum = n * (n+1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


# Problem 2: Find All Numbers Disappeared in an Array
def findDisappearedNumbers(nums):
    n = len(nums)
    full_set = set(range(1, n+1))
    given_set = set(nums)
    missing = full_set - given_set
    return list(missing)


# Problem 3: Valid Palindrome
def isPalindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# Tests
print("Missing Number:", missingNumber([3, 0, 1]))
print("Disappeared Numbers:", findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print("Valid Palindrome:", isPalindrome("A man, a plan, a canal: Panama"))