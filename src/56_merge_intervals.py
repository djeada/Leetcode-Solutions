class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return list()

        intervals.sort(key=lambda pair: pair[0])
        merged = [intervals[0]]
        
        for pair in intervals[1:]:
            # overlap
            if merged[-1][1] >= pair[0]:
                if pair[1] > merged[-1][1]:
                    merged[-1][1] = pair[1]
            # no overlap
            else:
                merged.append(pair)

        return merged
