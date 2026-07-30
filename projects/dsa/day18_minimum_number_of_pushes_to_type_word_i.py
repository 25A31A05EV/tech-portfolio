class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0

        for i in range(len(word)):
            ans += i // 8 + 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("abcde", 5),
        ("xycdefghij", 12),
        ("a", 1),
        ("abcdefgh", 8),
        ("abcdefghi", 10),
        ("abcdefghijklmnop", 24),
        ("abcdefghijklmnopqrstuvwx", 48),
        ("abcdefghijklmnopqrstuvwxyz", 56),
    ]

    for word, expected in test_cases:
        result = sol.minimumPushes(word)
        print(f"Input: {word}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print("Pass" if result == expected else "Fail")
        print("-" * 30)