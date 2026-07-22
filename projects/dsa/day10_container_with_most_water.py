# Day 10: Container With Most Water (Two Pointers)

def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        area = width * current_height
        max_area = max(max_area, area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area


# Test
print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))   # Output: 49