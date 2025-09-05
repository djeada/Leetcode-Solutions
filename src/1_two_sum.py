class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        for i, first in enumerate(nums):
            for j, second in enumerate(nums[i+1:], start=i+1):
                if first + second == target:
                    return [i, j]
        '''
        visited = dict()
        for i, num in enumerate(nums):
            complement =  target - num 
            if complement in visited:
                return [i, visited[complement]]

            visited[num] = i
