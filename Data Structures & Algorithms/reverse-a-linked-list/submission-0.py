# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head

        while current:
            # Capture and store the next node
            temp = current.next
            # Attach the next node to previous node
            current.next = prev
            # The previous node will now be the current node
            prev = current
            # The current node will be what the next node used to be
            current = temp
        return prev
