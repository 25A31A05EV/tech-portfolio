def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    left, right = 0, (m * n) - 1
    
    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n
        value = matrix[row][col]
        
        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False


# Test
matrix = [
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
print(searchMatrix(matrix, 3))   # True
print(searchMatrix(matrix, 13))  # False