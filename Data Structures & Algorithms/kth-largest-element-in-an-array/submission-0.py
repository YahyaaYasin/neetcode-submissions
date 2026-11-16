import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        maxHeap=[-num for num in nums]
        heapq.heapify(maxHeap)

        #base case
        if k > len(maxHeap):
            return 0

        out=None
        while k > 0:
            out=-heapq.heappop(maxHeap)
            k-=1

        return out
