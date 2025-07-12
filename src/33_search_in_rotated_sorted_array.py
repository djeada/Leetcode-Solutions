class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            i = (low + high) // 2
            middle = nums[i]
            if middle == target:
                return i

            if nums[low] <= middle:
                if nums[low] <= target <= nums[i]:
                    high = i - 1
                else:
                    low = i + 1
            else:
                if nums[i] <= target <=  nums[high]:
                    low = i + 1
                else:
                    high = i - 1

        return -1
