# Day 84 - Trapping Rain Water
# Pattern: Two Pointers
#
# Remember:
# Smaller side decides the water level.
# Compare left and right heights.
# Process the smaller side and move that pointer.

def trap(height):

    # Two pointers start from both ends
    left = 0
    right = len(height) - 1

    # Highest wall found from each side
    left_max = 0
    right_max = 0

    # Total trapped water
    water = 0

    # Continue until the two pointers meet
    while left < right:

        # If the left wall is smaller,
        # the left side is safe to process.
        if height[left] < height[right]:

            # Update left maximum if current wall is higher
            if height[left] >= left_max:
                left_max = height[left]

            # Otherwise, water can be trapped
            else:
                water += left_max - height[left]

            # Move left pointer
            left += 1

        # Otherwise, process the right side
        else:

            # Update right maximum if current wall is higher
            if height[right] >= right_max:
                right_max = height[right]

            # Otherwise, water can be trapped
            else:
                water += right_max - height[right]

            # Move right pointer
            right -= 1

    return water


# Example 1
height = [4, 2, 0, 3, 2, 5]

print("Height:", height)
print("Trapped Rain Water:", trap(height))


# Example 2
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print("Height:", height)
print("Trapped Rain Water:", trap(height))


# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Interview Trigger:
# "Trapping Rain Water"
#       ↓
# Two Pointers
#       ↓
# Compare left and right
#       ↓
# Smaller side
#       ↓
# Use left_max / right_max
#       ↓
# Calculate water
#       ↓
# Move pointer