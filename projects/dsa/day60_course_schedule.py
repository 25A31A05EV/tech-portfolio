def canFinish(numCourses, prerequisites):
    # Step 1: Build graph
    graph = {i: [] for i in range(numCourses)}

    for course, prereq in prerequisites:
        graph[course].append(prereq)

    # Step 2: Track current DFS path and completed courses
    visiting = set()
    visited = set()

    # Step 3: DFS cycle detection
    def dfs(course):
        # Course is already in current path → cycle
        if course in visiting:
            return False

        # Already completely checked
        if course in visited:
            return True

        visiting.add(course)

        # Check all prerequisites
        for prereq in graph[course]:
            if not dfs(prereq):
                return False

        # Remove from current path
        visiting.remove(course)

        # Mark as completely checked
        visited.add(course)

        return True

    # Step 4: Check every course
    for course in range(numCourses):
        if not dfs(course):
            return False

    return True


# Test Case 1
numCourses = 2
prerequisites = [[1, 0]]

print(canFinish(numCourses, prerequisites))
# Output: True


# Test Case 2
numCourses = 2
prerequisites = [[1, 0], [0, 1]]

print(canFinish(numCourses, prerequisites))
# Output: False