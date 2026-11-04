class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)
        vals = sorted(set(nums))
        m = len(vals)

        rank = {v: i + 1 for i, v in enumerate(vals)}

        count = [0] * (m + 1)
        total = [0] * (m + 1)

        def update(bit, i, delta):
            while i <= m:
                bit[i] += delta
                i += i & -i

        def query(bit, i):
            s = 0
            while i:
                s += bit[i]
                i -= i & -i
            return s

        def kth(target):
            idx = 0
            mask = 1 << (m.bit_length() - 1)

            while mask:
                nxt = idx + mask
                if nxt <= m and count[nxt] < target:
                    idx = nxt
                    target -= count[nxt]
                mask >>= 1

            return idx + 1

        costs = []

        for i in range(n):
            p = rank[nums[i]]
            update(count, p, 1)
            update(total, p, nums[i])

            if i >= x:
                old = rank[nums[i - x]]
                update(count, old, -1)
                update(total, old, -nums[i - x])

            if i >= x - 1:
                mid = kth((x + 1) // 2)
                median = vals[mid - 1]

                lc = query(count, mid)
                ls = query(total, mid)

                rc = x - lc
                rs = query(total, m) - ls

                cost = median * lc - ls + rs - median * rc
                costs.append(cost)

        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]
