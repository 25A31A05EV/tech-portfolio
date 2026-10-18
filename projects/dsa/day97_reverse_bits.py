
def reverseBits(n: int) -> int:
    result = 0

    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1

    return result


if __name__ == "__main__":
    assert reverseBits(43261596) == 964176192
    assert reverseBits(0) == 0
    assert reverseBits(1) == 2147483648

    print("All Day 97 tests passed!")
