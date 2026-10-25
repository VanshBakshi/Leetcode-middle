class Solution:
    def majorityElement(self, nums):
        count = {}
        n = len(nums)

        for num in nums:
            count[num] = count.get(num, 0) + 1

        result = []

        for num, freq in count.items():
            if freq > n // 3:
                result.append(num)

        return result
