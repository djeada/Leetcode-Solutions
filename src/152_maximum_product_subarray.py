class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        curr_max, curr_min, result = nums[0], nums[0], nums[0]

        for number in nums[1:]:
            if number < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(number, curr_max * number)
            curr_min = min(number, curr_min * number)

            result = max(curr_max, result)

        return result
        
