
def singleNumber(nums: list[int]) -> int:
    result = 0

    for num in nums:
        result ^= num

    return result


if __name__ == "__main__":
    assert singleNumber([2, 2, 1]) == 1
    assert singleNumber([4, 1, 2, 1, 2]) == 4
    assert singleNumber([1]) == 1
    assert singleNumber([7, 3, 7, 5, 5]) == 3

    print("All Day 94 tests passed!")
