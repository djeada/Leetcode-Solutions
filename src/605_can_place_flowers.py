class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # pad with an extra 0 on each side so we never have to special-case the ends
        padded = [0] + flowerbed + [0]
        total = 0
        
        # prev = “is the previous slot empty?”
        # curr = “is the current slot empty?”
        prev = (padded[0] == 0)
        curr = (padded[1] == 0)
        
        # now slide a window over padded[2:], which represents
        # “next” in each step
        for f in padded[2:]:
            # if all three are empty, we can plant in the middle
            if prev and curr and f == 0:
                total += 1
                # simulate planting: “middle” becomes occupied,
                # so for the next step we must pretend it was a 1
                prev = False  
                curr = True   # the “next” cell (f) is still empty
            else:
                # otherwise just slide the window forward
                prev = curr
                curr = (f == 0)
            
            if total >= n:
                return True
        
        return total >= n

