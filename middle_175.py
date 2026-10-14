class Solution:
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num:
            return ""

        result = ""

        while num > 0:
            digit = min(9, sum)
            result += str(digit)
            sum -= digit
            num -= 1

        return result
