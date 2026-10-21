class Solution:
    def minOperations(self, s):
        n = len(s)

        if s == ''.join(sorted(s)):
            return 0

        if n == 2:
            return -1

        if n == 3:
            return 1

        first = s[0]
        last = s[-1]
        mn = min(s)
        mx = max(s)

        if first == mx and last == mn:
            if all(c == first or c == last for c in s):
                return 3
            return 2

        if first == mx or last == mn:
            return 2

        if first == mn and last == mx:
            return 1

        return 2
