
class MaxHeap:

    def __init__(self):
        self._data = list()

    def push(self, num):
        heapq.heappush(self._data, -num)

    def pop(self):
        return -heapq.heappop(self._data)

    def top(self):
        return -self._data[0]

    def __len__(self):
        return len(self._data)


class MedianFinder:

    def __init__(self):
        self.lo = MaxHeap()
        self.up = list()

    def addNum(self, num: int) -> None:
        self.lo.push(num)
        val = self.lo.pop()
        heapq.heappush(self.up, val)

        if len(self.up) > len(self.lo):
            val = heapq.heappop(self.up)
            self.lo.push(val)

    def findMedian(self) -> float:
        if len(self.up) == len(self.lo):
            max_lo = self.lo.top()
            min_up = self.up[0]
            return (max_lo + min_up) / 2
        return self.lo.top()
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
