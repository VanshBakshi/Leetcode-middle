class Solution:
    def maximumGap(self, nums):
        n = len(nums)

        if n < 2:
            return 0

        mn = min(nums)
        mx = max(nums)

        if mn == mx:
            return 0

        size = max(1, (mx - mn) // (n - 1))
        count = (mx - mn) // size + 1

        bucket_min = [float('inf')] * count
        bucket_max = [float('-inf')] * count
        used = [False] * count

        for num in nums:
            idx = (num - mn) // size
            bucket_min[idx] = min(bucket_min[idx], num)
            bucket_max[idx] = max(bucket_max[idx], num)
            used[idx] = True

        ans = 0
        prev = mn

        for i in range(count):
            if used[i]:
                ans = max(ans, bucket_min[i] - prev)
                prev = bucket_max[i]

        return ans
