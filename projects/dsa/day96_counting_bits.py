
def countBits(n: int) -> list[int]:
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)

    return dp


if __name__ == "__main__":
    assert countBits(2) == [0, 1, 1]
    assert countBits(5) == [0, 1, 1, 2, 1, 2]
    assert countBits(0) == [0]

    print("All Day 96 tests passed!")
