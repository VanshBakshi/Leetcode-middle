class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)

        # Prefix sum
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        # Find next greater element
        nxt = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                nxt[i] = stack[-1]

            stack.append(i)

        # Binary lifting
        LOG = n.bit_length()

        up = [[n] * n for _ in range(LOG)]
        cost = [[0] * n for _ in range(LOG)]

        # Base level
        for i in range(n):
            j = nxt[i]
            up[0][i] = j

            cost[0][i] = (
                nums[i] * (j - i - 1)
                - (pref[j] - pref[i + 1])
            )

        # Build binary lifting tables
        for p in range(1, LOG):
            for i in range(n):
                mid = up[p - 1][i]

                if mid < n:
                    up[p][i] = up[p - 1][mid]
                    cost[p][i] = (
                        cost[p - 1][i]
                        + cost[p - 1][mid]
                    )
                else:
                    cost[p][i] = cost[p - 1][i]

        # Calculate operations needed for [l, r]
        def getCost(l, r):
            total = 0
            cur = l

            for p in range(LOG - 1, -1, -1):
                if up[p][cur] <= r:
                    total += cost[p][cur]
                    cur = up[p][cur]

            total += (
                nums[cur] * (r - cur)
                - (pref[r + 1] - pref[cur + 1])
            )

            return total

        # Sliding window
        ans = 0
        left = 0

        for right in range(n):
            while getCost(left, right) > k:
                left += 1

            ans += right - left + 1

        return ans
