# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        nodes = 1
        curr = head

        while curr.next is not None:
            
            curr = curr.next
            nodes += 1

        pre_index = nodes - n - 1

        if n == nodes and pre_index == -1:
            return head.next

        curr = head
        
        while pre_index > 0:
            curr = curr.next
            pre_index -= 1

        temp = curr.next

        if temp is None:
            curr = None
        else:
            curr.next = temp.next

        return head

        
        