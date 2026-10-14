def missingNumber(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


if __name__ == "__main__":
    assert missingNumber([3, 0, 1]) == 2
    assert missingNumber([0, 1]) == 2
    assert missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8

    print("All tests passed!")