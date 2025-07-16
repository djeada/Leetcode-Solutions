class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()

        def backtrack(start, remaining_target, path):
            if remaining_target == 0:
                results.append(path.copy())
                return

            if remaining_target < 0:
                return

            for i in range(start, len(candidates)):
                candidate = candidates[i]
                if candidate > remaining_target:
                    return
                
                path.append(candidate)
                backtrack(i, remaining_target - candidate, path)
                path.pop() 

        backtrack(0, target, [])
        return results
