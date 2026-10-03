class Solution:
    def restoreIpAddresses(self, s):
        result = []

        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    result.append(".".join(parts))
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start + length]

                # Leading zero is not allowed
                if len(part) > 1 and part[0] == '0':
                    break

                # IP segment must be between 0 and 255
                if int(part) > 255:
                    break

                backtrack(start + length, parts + [part])

        backtrack(0, [])
        return result
