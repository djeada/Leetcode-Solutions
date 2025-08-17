class Solution:



    def countBits(self, n: int) -> List[int]:
        '''
        def _countBits(number):
            count = 0

            while number:
                count += (number & 1)
                number >>= 1

            return count


        result = [0] * (n + 1)

        for i in range(1, n + 1):
            result[i] = _countBits(i)

        return result
        '''

        result = [0] * (n + 1)

        for i in range(1, n + 1):
            result[i] = result[i >> 1] + (i & 1)

        return result
