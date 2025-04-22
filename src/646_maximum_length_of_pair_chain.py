from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # 1) Sort all pairs by their right endpoint (ascending)
        pairs_sorted = sorted(pairs, key=lambda interval: interval[1])
        
        # 2) Greedily build the longest chain
        chain_length = 0
        current_chain_end = -10**9  # smaller than any possible left_i
        
        for left, right in pairs_sorted:
            # Only start a new link if it strictly follows the last one
            if left > current_chain_end:
                chain_length += 1
                current_chain_end = right
        
        return chain_length
