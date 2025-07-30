class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        left = [
            interval for interval in intervals if 
            interval[1] < newInterval[0]
        ]

        right = [
            interval for interval in intervals if 
            interval[0] > newInterval[1]
        ]

        middle = [
            interval for interval in intervals if 
            not (
                interval[1] < newInterval[0] 
                or interval[0] > newInterval[1]
            )
        ] + [newInterval]

        middle = [
            min(interval[0] for interval in middle),
            max(interval[1] for interval in middle)
        ]

        return left + [middle] + right
        
