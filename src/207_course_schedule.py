class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
                # Build adjacency list: for each course, list of courses that depend on it
        adjacency_list = [[] for _ in range(numCourses)]
        # in_degree[c] = number of prerequisites course c has
        in_degree = [0] * numCourses

        # Populate adjacency and in-degree counts
        for course, prereq in prerequisites:
            adjacency_list[prereq].append(course)
            in_degree[course] += 1

        # Initialize queue with all courses that have no prerequisites
        courses_queue = deque(
            course for course in range(numCourses) if in_degree[course] == 0
        )

        courses_completed = 0

        # Process courses in topological order
        while courses_queue:
            current = courses_queue.popleft()
            courses_completed += 1

            # "Take" this course, decrement in-degree of dependent courses
            for dependent in adjacency_list[current]:
                in_degree[dependent] -= 1
                # If all prerequisites for dependent are satisfied, enqueue it
                if in_degree[dependent] == 0:
                    courses_queue.append(dependent)

        # If we've completed all courses, there was no cycle
        return courses_completed == numCourses
