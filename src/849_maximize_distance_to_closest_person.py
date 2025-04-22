import math
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)

        # leading zeros (from the left edge up to the first 1)
        first_one = seats.index(1)
        leading_distance = first_one
        
        # trailing zeros (from the last 1 to the right edge)
        last_one = n - 1 - seats[::-1].index(1)
        trailing_distance = n - 1 - last_one
        
        # middle zeros
        max_distance = 0
        current_distance = 0
        for s in seats:
            if s == 1:
                if current_distance > max_distance:
                    max_distance = current_distance
                current_distance = 0
            else:
                current_distance += 1

        return max(leading_distance, trailing_distance, math.ceil(max_distance/2))
