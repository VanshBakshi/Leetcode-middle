class Solution:
    def kthSmallest(self, root, k):
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            k -= 1

            if k == 0:
                return current.val

            current = current.right
          
