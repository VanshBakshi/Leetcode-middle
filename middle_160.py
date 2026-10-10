class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left = 0
        right = max(diff)

        while left < right:
            mid = (left + right) // 2
            need = sum(max(0, x - mid) for x in diff)

            if need <= k:
                right = mid
            else:
                left = mid + 1

        level = left
        need = sum(max(0, x - level) for x in diff)

        diff = [min(x, level) for x in diff]

        for i in range(len(diff)):
            if need < k and diff[i] == level and level > 0:
                diff[i] -= 1
                need += 1

            if need == k:
                break

        return sum(x * x for x in diff)
      
