class Solution:
    POP_COUNT = [bin(i).count('1') for i in range(2**8)] # every 8 bit number

    def hammingWeight(self, n: int) -> int:
        '''
        result = 0

        while n:
            result += (n & 1)
            n >>= 1

        return result
        '''

        return self.POP_COUNT[n & 0xFF] +  self.POP_COUNT[(n >> 8) & 0xFF] + self.POP_COUNT[(n >> 16) & 0xFF] + self.POP_COUNT[(n >> 24) & 0xFF] 

        
