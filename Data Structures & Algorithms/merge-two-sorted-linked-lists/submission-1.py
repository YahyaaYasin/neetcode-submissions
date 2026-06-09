# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Base cases
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        curr1 = list1
        curr2 = list2

        # assign the main head
        main = None
        if curr1.val <= curr2.val:
            main = curr1
            curr1 = curr1.next
        else:
            main = curr2
            curr2 = curr2.next

        # keep track of the head
        out = main

        # main loop
        while curr1 is not None and curr2 is not None:

            if curr2.val <= curr1.val:
                main.next = curr2
                curr2 = curr2.next

            elif curr1.val <= curr2.val:
                main.next = curr1
                curr1 = curr1.next

            main = main.next

        if curr1 is None:
            main.next = curr2
        elif curr2 is None:
            main.next = curr1

        return out 

