class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Break the list into left and right parts
        prev.next = None

        root = TreeNode(slow.val)

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root
