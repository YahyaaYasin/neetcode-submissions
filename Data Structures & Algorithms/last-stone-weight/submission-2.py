import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        #inverse the numbers to create a max heap
        maxHeap=[-stone for stone in stones]

        #heapify the maxHeap
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:

            s1=-heapq.heappop(maxHeap)
            s2=-heapq.heappop(maxHeap)

            if s1==s2:
                continue
            else:
                difference=-(max(s1,s2)-min(s1,s2))
                heapq.heappush(maxHeap, difference)


        if not maxHeap:
            return 0
        else:
            return -maxHeap[0]


        


        