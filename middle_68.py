class Solution:
    def recoverTree(self, root):

        first = None
        second = None
        prev = None

        curr = root

        while curr:

            if curr.left is None:
                # Visit current node
                if prev and prev.val > curr.val:
                    if first is None:
                        first = prev

                    second = curr

                prev = curr
                curr = curr.right

            else:
                # Find inorder predecessor
                predecessor = curr.left

                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    # Create temporary link
                    predecessor.right = curr
                    curr = curr.left

                else:
                    # Remove temporary link
                    predecessor.right = None

                    # Visit current node
                    if prev and prev.val > curr.val:
                        if first is None:
                            first = prev

                        second = curr

                    prev = curr
                    curr = curr.right

        # Swap the values
        first.val, second.val = second.val, first.val
