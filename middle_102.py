class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        pos = {value: i for i, value in enumerate(inorder)}

        def build(pre_start, in_start, in_end):
            if in_start > in_end:
                return None

            root_value = preorder[pre_start]
            root = TreeNode(root_value)

            mid = pos[root_value]
            left_size = mid - in_start

            root.left = build(
                pre_start + 1,
                in_start,
                mid - 1
            )

            root.right = build(
                pre_start + left_size + 1,
                mid + 1,
                in_end
            )

            return root

        return build(0, 0, len(inorder) - 1)
