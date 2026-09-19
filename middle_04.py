class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x > 0:
            digit = x % 10
            x //= 10

            # Check 32-bit overflow before adding digit
            if rev > 214748364 or (rev == 214748364 and digit > 7):
                return 0

            rev = rev * 10 + digit

        return sign * rev
