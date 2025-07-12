class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) -1

        if nums[low] <= nums[high]:
            return nums[low]

        while low < high:
            middle = (low + high) // 2
            if nums[middle] > nums[high]:
                low = middle + 1
            else:
                high = middle

        return nums[low]
        
