class Solution(object):
    def maxPoints(self, points):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(points)

        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slopes = {}
            best = 0

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx == 0:
                    slope = (0, 1)
                elif dy == 0:
                    slope = (1, 0)
                else:
                    g = gcd(abs(dx), abs(dy))
                    dx //= g
                    dy //= g

                    if dx < 0:
                        dx = -dx
                        dy = -dy

                    slope = (dx, dy)

                slopes[slope] = slopes.get(slope, 0) + 1
                best = max(best, slopes[slope])

            ans = max(ans, best + 1)

        return ans
