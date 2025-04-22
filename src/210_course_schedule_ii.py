from collections import deque
from typing import List

class Solution:
    def findOrder(self, number_of_courses: int, prereq_pairs: List[List[int]]) -> List[int]:
        # Build adjacency list: for each course, list of courses that depend on it
        adjacency_list = [[] for _ in range(number_of_courses)]
        # in_degree[c] = number of prerequisites c has
        in_degree = [0] * number_of_courses

        # Populate adjacency and in-degree counts
        for course, prereq in prereq_pairs:
            adjacency_list[prereq].append(course)
            in_degree[course] += 1

        # Initialize queue with all courses that have no prerequisites
        courses_queue = deque(
            course for course in range(number_of_courses) if in_degree[course] == 0
        )

        course_order: List[int] = []

        # Process courses in topological order
        while courses_queue:
            current_course = courses_queue.popleft()
            course_order.append(current_course)

            # "Take" this course, decrement in-degree of dependent courses
            for next_course in adjacency_list[current_course]:
                in_degree[next_course] -= 1
                # If all prerequisites for next_course are satisfied, enqueue it
                if in_degree[next_course] == 0:
                    courses_queue.append(next_course)

        # If we've ordered all courses, return the sequence; otherwise, there's a cycle
        if len(course_order) == number_of_courses:
            return course_order
        else:
            return []
