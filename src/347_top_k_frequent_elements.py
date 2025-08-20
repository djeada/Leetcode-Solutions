
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        max_f = max(counter.values())
        buckets = [[] for i in range(max_f + 1)]

        for num, freq in counter.items():
            buckets[freq].append(num)

        result = list()
        for bucket in reversed(buckets):
            for num in bucket:
                result.append(num)
                if len(result) == k:
                    return result

        return list()
