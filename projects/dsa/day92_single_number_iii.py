
def singleNumber(nums):
    xor_all = 0
    for num in nums:
        xor_all ^= num

    rightmost_bit = xor_all & -xor_all

    num1 = 0
    num2 = 0

    for num in nums:
        if num & rightmost_bit:
            num1 ^= num
        else:
            num2 ^= num

    return [num1, num2]


if __name__ == "__main__":
    assert set(singleNumber([1, 2, 1, 3, 2, 5])) == {3, 5}
    assert set(singleNumber([-1, 0])) == {-1, 0}
    assert set(singleNumber([0, 1])) == {0, 1}
    assert set(singleNumber([4, 4, 6, 7])) == {6, 7}

    print("All Day 92 tests passed!")
