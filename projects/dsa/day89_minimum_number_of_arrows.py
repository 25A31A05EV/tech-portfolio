class Solution:

    def findMinArrowShots(self, points: list[list[int]]) -> int:

        if not points:
            return 0

        # Sort balloons by ending position
        points.sort(key=lambda balloon: balloon[1])

        # Shoot the first arrow at the first balloon's end
        arrows = 1
        arrow_position = points[0][1]

        # Process remaining balloons
        for start, end in points[1:]:

            # If the balloon starts after the current arrow,
            # we need a new arrow
            if start > arrow_position:
                arrows += 1
                arrow_position = end

        return arrows


# Test the solution
if __name__ == "__main__":
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]

    solution = Solution()
    print(solution.findMinArrowShots(points))