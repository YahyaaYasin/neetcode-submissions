import heapq, math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        #calculate the euclidean distance and add them in a min heap and a dictionary with thier x,y values
        minHeap=[]
        heapq.heapify(minHeap)

        for x,y in points:
            
            distance= math.sqrt( ((x) ** 2) + ((y) ** 2) )
            heapq.heappush(minHeap,distance)

        #pop the min heap k times to get their x,y values from the book
        kVals=[]
        while k > 0:
            val=heapq.heappop(minHeap)
            kVals.append(val)
            k-=1

        # get the x,y coordinates of the k values
        set(kVals)
        out=[]

        for x,y in points:

            distance= math.sqrt( ((x) ** 2) + ((y) ** 2) )
            if distance in kVals:
                out.append([x,y])

        return out

        