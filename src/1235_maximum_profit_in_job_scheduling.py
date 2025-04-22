class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # 1. Pair up and sort jobs by their end time
        jobs_sorted = sorted(
            zip(startTime, endTime, profit),
            key=lambda job: job[1]
        )

        # Extract the sorted end times for binary search
        sorted_end_times = [job_end for _, job_end, _ in jobs_sorted]

        n_jobs = len(jobs_sorted)
        # max_profit[i] = best profit using the first i jobs in jobs_sorted
        # (we use 1-based indexing, so max_profit[0] = 0)
        max_profit = [0] * (n_jobs + 1)

        for i in range(1, n_jobs + 1):
            curr_start, curr_end, curr_profit = jobs_sorted[i - 1]

            # 2. Find the rightmost job that finishes <= curr_start
            # bisect_right gives the insertion index, so that's exactly
            # how many jobs end <= curr_start
            compatible_index = bisect_right(sorted_end_times, curr_start)

            # Option A: skip this job → profit = max_profit[i-1]
            skip_profit = max_profit[i - 1]
            # Option B: take this job → profit = max_profit[compatible_index] + curr_profit
            take_profit = max_profit[compatible_index] + curr_profit

            # 3. Choose the better of the two
            max_profit[i] = max(skip_profit, take_profit)

        # Answer is the best profit using all jobs
        return max_profit[n_jobs]
