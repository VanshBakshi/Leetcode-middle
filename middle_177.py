
class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        tree1 = [0] * (4 * n)
        tree2 = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(node, start, end, left, right):
            if left <= start and end <= right:
                length = end - start + 1
                d = 1

                tree2[node] = (
                    tree2[node]
                    + 2 * d * tree1[node]
                    + length * d * d
                ) % MOD

                tree1[node] = (tree1[node] + length * d) % MOD
                lazy[node] += d
                return

            mid = (start + end) // 2
            push(node, start, end)

            if left <= mid:
                update(node * 2, start, mid, left, right)
            if right > mid:
                update(node * 2 + 1, mid + 1, end, left, right)

            tree1[node] = (
                tree1[node * 2] + tree1[node * 2 + 1]
            ) % MOD

            tree2[node] = (
                tree2[node * 2] + tree2[node * 2 + 1]
            ) % MOD

        def push(node, start, end):
            if lazy[node] == 0 or start == end:
                return

            mid = (start + end) // 2
            d = lazy[node]

            for child, length in (
                (node * 2, mid - start + 1),
                (node * 2 + 1, end - mid),
            ):
                tree2[child] = (
                    tree2[child]
                    + 2 * d * tree1[child]
                    + length * d * d
                ) % MOD

                tree1[child] = (
                    tree1[child] + length * d
                ) % MOD

                lazy[child] += d

            lazy[node] = 0

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            left = last.get(x, -1) + 1

            # Increase distinct counts for subarrays
            # ending at index i.
            update(1, 0, n - 1, left, i)

            ans = (ans + tree2[1]) % MOD
            last[x] = i

        return ans
