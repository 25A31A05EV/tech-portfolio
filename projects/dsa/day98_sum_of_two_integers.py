
def getSum(a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    MAX_INT = 0x7FFFFFFF

    while b:
        carry = (a & b) << 1
        a = (a ^ b) & MASK
        b = carry & MASK

    return a if a <= MAX_INT else ~(a ^ MASK)


if __name__ == "__main__":
    assert getSum(2, 3) == 5
    assert getSum(2, -3) == -1
    assert getSum(-1, 1) == 0
    assert getSum(-12, -8) == -20
    assert getSum(0, 0) == 0

    print("All Day 98 tests passed!")
