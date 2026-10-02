
class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                duplicate = curr.val

                while curr and curr.val == duplicate:
                    curr = curr.next

                prev.next = curr

            else:
                prev = curr
                curr = curr.next

        return dummy.next
