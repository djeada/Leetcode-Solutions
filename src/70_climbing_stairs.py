class Solution:
    def climbStairs(self, n: int) -> int:
                # Base cases: for n = 1 or 2, the answer is n itself
        if n <= 2:
            return n

        # ways_two_back = ways to reach stair i-2
        # ways_one_back = ways to reach stair i-1
        ways_two_back, ways_one_back = 1, 2

        # Build up from stair 3 to n
        for stair in range(3, n + 1):
            ways_current = ways_one_back + ways_two_back
            # Slide the window forward
            ways_two_back, ways_one_back = ways_one_back, ways_current

        # ways_one_back now holds ways to reach stair n
        return ways_one_back
