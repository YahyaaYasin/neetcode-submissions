# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # base case
        if not lists:
            return None
                    
        # update the list by removing the ll's that is finished
        lists = [node for node in lists if node is not None]
        ul = []         # get a updated list of val's
        for node in lists:
            ul.append(node.val)

        # get the index of min from the updated list of val's
        ind = ul.index(min(ul))

        # assign a head and tail
        head = lists[ind]
        tail = head

        # update the ll that was taken as head to move to the next node
        if lists[ind].next != None:
                lists[ind] = lists[ind].next
        else:
            lists[ind] = None

        while True:
            
            # update the list by removing the ll's that is finished
            lists = [node for node in lists if node is not None]
            ul = []         # get a updated list of val's
            for node in lists:
                ul.append(node.val)

            # break of list is empty meaning no more ll left to merge
            if len(lists) < 1:
                break

            # get the index of min from the updated list of val's
            ind = ul.index(min(ul))

            # move the tail forward 
            tail.next = lists[ind]
            tail = tail.next

            # update the ll that was just merged to move to the next node
            if lists[ind].next != None:
                lists[ind] = lists[ind].next
            else:
                lists[ind] = None

        return head



