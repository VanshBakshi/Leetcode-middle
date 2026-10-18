class Solution:
    def numOfWays(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute combinations C(n, k)
        comb = [[0] * n for _ in range(n)]

        for i in range(n):
            comb[i][0] = 1
            comb[i][i] = 1

            for j in range(1, i):
                comb[i][j] = (comb[i - 1][j - 1] +
                              comb[i - 1][j]) % MOD

        def solve(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]

            l = len(left)
            r = len(right)

            ways_left = solve(left)
            ways_right = solve(right)

            # Interleave left and right while preserving
            # the relative order within each subtree.
            return (comb[l + r][l] * ways_left *
                    ways_right) % MOD

        # Exclude the original ordering
        return (solve(nums) - 1) % MOD
