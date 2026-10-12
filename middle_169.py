class Solution:
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        bits = [0] * 30

        for num in nums:
            for i in range(30):
                if num & (1 << i):
                    bits[i] += 1

        ans = 0

        for _ in range(k):
            num = 0

            for i in range(30):
                if bits[i] > 0:
                    num |= (1 << i)
                    bits[i] -= 1

            ans = (ans + num * num) % MOD

        return ans
