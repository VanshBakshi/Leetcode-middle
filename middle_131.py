class Solution:
    def partition(self, s):
        result = []
        current = []

        def isPalindrome(text):
            return text == text[::-1]

        def backtrack(start):
            if start == len(s):
                result.append(current[:])
                return

            for end in range(start, len(s)):
                part = s[start:end + 1]

                if isPalindrome(part):
                    current.append(part)

                    backtrack(end + 1)

                    current.pop()

        backtrack(0)

        return result
