class Solution:
    def countNodes(self, root):
        if not root:
            return 0

        left = root.left
        right = root.right

        left_height = 0
        right_height = 0

        while left:
            left_height += 1
            left = left.left

        while right:
            right_height += 1
            right = right.right

        if left_height == right_height:
            return (1 << (left_height + 1)) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
