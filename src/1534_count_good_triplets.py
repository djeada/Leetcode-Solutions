class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        good_triplet_count = 0

        # Enumerate all triples i < j < k
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                # Early check for the first condition
                if abs(arr[i] - arr[j]) > a:
                    continue

                for k in range(j + 1, n):
                    # Check the remaining two conditions
                    if abs(arr[j] - arr[k]) <= b and \
                       abs(arr[i] - arr[k]) <= c:
                        good_triplet_count += 1

        return good_triplet_count
