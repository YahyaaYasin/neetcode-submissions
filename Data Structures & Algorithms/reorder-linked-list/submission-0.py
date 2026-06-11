# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Base case
        if head is None:
            return None

        # track of all nodes
        track = []

        curr = head
        while curr is not None:

            add_of_curr = curr
            track.append(add_of_curr)

            curr = curr.next

        first = 0
        last = len(track) - 1

        while first < last:

            track[first].next = track[last]
            track[last].next = track[first+1]

            first += 1
            last -= 1

        track[first].next = None

        

        

            

        

        

        