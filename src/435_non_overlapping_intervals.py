class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x:x[1]) # sort by second element

        prev_start, prev_end = intervals[0]
        counter = 1 # keeps track of how many intervals we keep
        
        for curr_start, curr_end in intervals[1:]:
            if prev_end <= curr_start:
                counter += 1
                prev_end = curr_end

        return len(intervals) - counter
