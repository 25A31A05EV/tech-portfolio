class Solution:

    def findDuplicate(self, nums: list[int]) -> int:

        # --------------------------------------------------
        # Problem:
        # Find the number that appears more than once.
        #
        # Example:
        # nums = [1, 3, 4, 2, 2]
        # Answer = 2
        #
        # We use Floyd's Cycle Detection Algorithm.
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # --------------------------------------------------

        # --------------------------------------------------
        # PHASE 1: Find the meeting point
        #
        # Think of every number as the next index.
        #
        # Example:
        # [1, 3, 4, 2, 2]
        #
        # 0 -> 1 -> 3 -> 2 -> 4 -> 2 -> 4...
        #
        # Because 2 is repeated, a cycle is created.
        # --------------------------------------------------

        slow = nums[0]
        fast = nums[0]

        while True:

            # Slow moves one step
            slow = nums[slow]

            # Fast moves two steps
            fast = nums[nums[fast]]

            # When both meet, we found the cycle
            if slow == fast:
                break

        # --------------------------------------------------
        # PHASE 2: Find the entrance of the cycle
        #
        # Reset slow to the beginning.
        # Keep fast at the meeting point.
        #
        # Now move both one step at a time.
        # Their meeting point is the duplicate number.
        # --------------------------------------------------

        slow = nums[0]

        while slow != fast:

            # Move both one step
            slow = nums[slow]
            fast = nums[fast]

        # The meeting point is the duplicate number
        return slow