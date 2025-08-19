class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        def rob_street(houses):
            skip, take = 0, 0

            for house in houses:
                skip, take = max(skip, take), skip + house

            return max(skip, take)


        return max(
            rob_street(nums[1:]),
            rob_street(nums[:-1])
            )
