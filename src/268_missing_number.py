class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # Option 1:  using arithmetic sequence
        # n = len(nums)
        # sum_nums = sum(nums)
        # s_n = n*(n + 1) // 2
        # return s_n - sum_nums


        # Option 2: using XOR
        n = len(nums)
        x = n

        for i, num in enumerate(nums):
            x ^= i ^ num

        return x
