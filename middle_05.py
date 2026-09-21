class Solution:
    def resultArray(self, nums, k):
        result = [0] * k

        # dp[r] = number of subarrays ending at the previous position
        # whose product % k == r
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Start a new subarray with just nums[i]
            r = num % k
            new_dp[r] += 1

            # Extend every previous subarray
            for old_r in range(k):
                if dp[old_r] > 0:
                    new_r = (old_r * r) % k
                    new_dp[new_r] += dp[old_r]

            # Every subarray ending here contributes to the answer
            for r in range(k):
                result[r] += new_dp[r]

            dp = new_dp

        return result
