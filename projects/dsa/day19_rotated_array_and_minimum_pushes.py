# -----------------------------------------
# Day 19
# Problem 1: Rotate Array (LeetCode 189)
# Topic: Array
# -----------------------------------------

def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums


# Test Cases
print("Rotate Array Test Cases")
print(rotate([1, 2, 3, 4, 5, 6, 7], 3))      # [5,6,7,1,2,3,4]
print(rotate([-1, -100, 3, 99], 2))          # [3,99,-1,-100]
print(rotate([1], 0))                        # [1]
print()


# -----------------------------------------
# Problem 2:
# Minimum Number of Pushes to Type Word II
# (LeetCode 3016)
# Topic: Greedy
# -----------------------------------------

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26

        # Count frequency of each character
        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        # Sort frequencies in descending order
        freq.sort(reverse=True)

        pushes = 0

        # Calculate minimum pushes
        for i, f in enumerate(freq):
            if f == 0:
                break
            pushes += f * (i // 8 + 1)

        return pushes


# Test Cases
obj = Solution()

print("Minimum Pushes Test Cases")
print(obj.minimumPushes("abcde"))          # 5
print(obj.minimumPushes("xycdefghij"))     # 12
print(obj.minimumPushes("aabbcc"))         # 6
print(obj.minimumPushes("abcdefghijkl"))   # 16