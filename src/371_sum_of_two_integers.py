class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = (1 << 32) - 1
        MAX = (1 << 31) - 1

        _sum = (a ^ b) & MASK
        carry = ((a & b) << 1) & MASK
        
        while b != 0:
            _sum = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK
            a, b = _sum, carry
    
        if _sum > MAX:
            return ~(_sum ^ MASK)
        
        return _sum
