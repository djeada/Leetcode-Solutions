class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        while matrix:
            row = matrix.pop(0)
            result.extend(row)

            # ccw 90 rotation
            matrix = [
                row for row in 
                reversed(list(zip(*matrix)))
            ]

        return result
        
        
