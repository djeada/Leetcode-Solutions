class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curr_sum, best_sum = nums[0], nums[0]

        for num in nums[1:]:
            if curr_sum < 0:
                curr_sum = num
            else:
                curr_sum += num

            if curr_sum > best_sum:
                best_sum = curr_sum

        return best_sum
