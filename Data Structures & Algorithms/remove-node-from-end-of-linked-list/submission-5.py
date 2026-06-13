# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        nodes = 1
        curr = head

        # Get count of the number of nodes

        while curr.next is not None:
            
            curr = curr.next
            nodes += 1

        # calculate the index of the prevous node of the node that will be removed
        pre_index = nodes - n - 1

        # handle the edge case where we are removing the first node
        if n == nodes and pre_index == -1:
            return head.next

        # go to the previous node
        
        curr = head
        while pre_index > 0:
            curr = curr.next
            pre_index -= 1

        # keep track of the soon to be removed node
        temp = curr.next

        #if the next node is empty, make it point to none 
        if temp is None:
            curr.next = None
        
        # assign the previous nodes pointer to point to the next-next
        else:
            curr.next = temp.next

        return head

        
        