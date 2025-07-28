class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        furthest = 0

        for i, step in enumerate(nums):
            if i > furthest:
                return False

            if furthest <  i + step:
               furthest = i + step

            if furthest >= n - 1:
                return True

        return furthest >= n - 1
        
