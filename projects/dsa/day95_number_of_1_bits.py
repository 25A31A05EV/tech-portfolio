
def hammingWeight(n: int) -> int:
    count = 0

    while n:
        n &= n - 1
        count += 1

    return count


if __name__ == "__main__":
    assert hammingWeight(11) == 3
    assert hammingWeight(128) == 1
    assert hammingWeight(2147483645) == 30
    assert hammingWeight(0) == 0

    print("All Day 95 tests passed!")
