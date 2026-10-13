class Solution:
    def maxAlternatingSum(self, nums):
        nums = sorted(x * x for x in nums)
        n = len(nums)
        k = (n + 1) // 2

        return sum(nums[n - k:]) - sum(nums[:n - k])
