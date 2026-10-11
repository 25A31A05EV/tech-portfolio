from collections import Counter


class Solution:

    def leastInterval(self, tasks: list[str], n: int) -> int:

        # Count the frequency of each task
        freq = Counter(tasks)

        # Find the maximum task frequency
        max_freq = max(freq.values())

        # Count how many tasks have the maximum frequency
        count_max = sum(
            1 for count in freq.values()
            if count == max_freq
        )

        # Calculate the minimum intervals using the greedy formula
        intervals = (max_freq - 1) * (n + 1) + count_max

        # Either use idle intervals or execute tasks consecutively
        return max(len(tasks), intervals)


# Test the solution
if __name__ == "__main__":

    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2

    solution = Solution()
    print(solution.leastInterval(tasks, n))