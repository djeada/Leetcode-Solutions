class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sorted_nums = sorted(nums)
        found = set()

        for i in range(n-2):
            if sorted_nums[i] > 0:
                break
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                triplet_sum = sorted_nums[i] +  sorted_nums[j] +  sorted_nums[k]
                if triplet_sum == 0:
                    found.add((sorted_nums[i], sorted_nums[j], sorted_nums[k]))
                    j += 1
                    k -= 1
                elif triplet_sum < 0:
                    j += 1
                # triplet_sum > 0
                else:
                    k -= 1

        return [list(triplet) for triplet in found]
